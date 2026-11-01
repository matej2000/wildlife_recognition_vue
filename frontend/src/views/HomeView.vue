<script setup>
import Models from '../components/home_page/Models.vue'
import CameraTrapLocations from '@/components/home_page/CameraTrapLocations.vue';
import ModelCapabilities from '@/components/home_page/ModelCapabilities.vue';
import AnimalSpecies from '@/components/home_page/AnimalSpecies.vue';
import Navbar from '@/components/Navbar.vue';
import HeroSection from '@/components/home_page/HeroSection.vue';
</script>

<template>
  <main class="w-full">

    <HeroSection/>
    
    <CameraTrapLocations />

    <a id="models"></a>
    <Models />
    
    <a id="capabilities"></a>
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
