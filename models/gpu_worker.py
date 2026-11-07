import asyncio


class GPUWorker:
    def __init__(self, gpu_manager):
        self.gpu_manager = gpu_manager
        self.queue = asyncio.Queue(maxsize=10)
        self.worker_task = None

    async def start(self):
        self.worker_task = asyncio.create_task(self._run())

    async def stop(self):
        if self.worker_task:
            self.worker_task.cancel()

            try:
                await self.worker_task
            except asyncio.CancelledError:
                pass

    async def submit(self, model_name, data):
        loop = asyncio.get_running_loop()
        future = loop.create_future()

        await self.queue.put({"model_name": model_name, "data": data, "future": future})

        return await future

    async def _run(self):
        while True:
            request = await self.queue.get()

            try:
                result = await asyncio.to_thread(
                    self.gpu_manager.predict, request["model_name"], request["data"]
                )

                if not request["future"].done():
                    request["future"].set_result(result)

            except Exception as e:
                if not request["future"].done():
                    request["future"].set_exception(e)

            finally:
                self.queue.task_done()
