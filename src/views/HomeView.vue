<script setup>
import Models from '../components/home_page/Models.vue'
import CameraTrapLocations from '@/components/home_page/CameraTrapLocations.vue';
import ModelCapabilities from '@/components/home_page/ModelCapabilities.vue';
import AnimalSpecies from '@/components/home_page/AnimalSpecies.vue';
import Navbar from '@/components/Navbar.vue';
</script>

<template>
  <header>
    <Navbar class=""></Navbar>
  </header>
  <main class="w-full">
    <!-- after:content-[mask-image:url(/curve-2.svg)] [mask-repeat:no-repeat] -->
    <div class="relative w-full align-center m-auto bg-[url(beautiful-shot-cute-deer-forest.jpg)] h-[600px] sm:h-[800px] bg-cover bg-[70%_50%] md:bg-center">
        <div class="w-full h-full bg-black opacity-30 z-10"></div>
        <div class="absolute top-2/3 sm:top-1/2 left-1/2 font-serif text-white text-center text-4xl font-bold sm:text-7xl md:text-8xl -translate-x-1/2 -translate-y-1/2 whitespace-nowrap">
          <div>Wildlife</div>
          <div>
            Recognition AI
          </div>
        </div>
        <!-- <div class="absolute w-full bottom-0 -translate-y-1/2 z-1">
          <img src="/curve-2.svg" class="">
        </div> -->
    </div>

    <Models />
    
    <CameraTrapLocations />

    <ModelCapabilities />
   
    <AnimalSpecies />
  </main>
</template>


<script>
import { useAuthStore } from '../store/auth.js'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const authStore = useAuthStore()
    const router = useRouter()

    return {
      authStore, router
    }
  },
  methods: {
    async logout() {
      try {
        await this.authStore.logout(this.$router)
      } catch (error) {
        console.error(error)
      }
    }
  },
  async mounted() {
    await this.authStore.fetchUser()
  }
}
</script>
