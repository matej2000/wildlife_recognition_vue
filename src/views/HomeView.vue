<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main class="w-full">
    <div class="w-full align-center m-auto bg-[url(beautiful-shot-cute-deer-forest.jpg)] h-[600px] sm:h-[800px] bg-cover bg-[70%_50%] md:bg-center">
        <div class="w-full h-full bg-black opacity-30 z-10"></div>
        <!-- <div class="w-auto h-auto text-white text-8xl lg:text-9xl absolute top-1/2 left-1/2 lg:top-1/2 lg:left-1/2 font-serif overflow-hidden"> -->
        <div class="absolute top-2/3 sm:top-1/2 left-1/2 font-serif text-white text-center text-4xl font-bold sm:text-7xl md:text-8xl -translate-x-1/2 -translate-y-1/2 whitespace-nowrap">
          <div>Wildlife</div>
          <div>
            Recognition AI
          </div>
        </div>
    </div>
    <TheWelcome />
  </main>
</template>
