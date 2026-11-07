from model_registry import MODEL_REGISTRY


class GPUManager:
    def __init__(self):
        self.models = {
            name: model_class() for name, model_class in MODEL_REGISTRY.items()
        }
        self.active_model = None
        self.active_model_name = None

    def get_model(self, model_name):

        if model_name not in MODEL_REGISTRY:
            raise ValueError(f"Unknown model: {model_name}")

        if model_name not in self.models:
            self.models[model_name] = MODEL_REGISTRY[model_name]()

        return self.models[model_name]

    def predict(self, model_name, data):

        if model_name != self.active_model_name:

            if self.active_model is not None:
                self.active_model.unmount()

            self.active_model = None
            self.active_model_name = None

            model = self.get_model(model_name)
            model.mount()

            self.active_model = model
            self.active_model_name = model_name

        return self.active_model.predict(data)
