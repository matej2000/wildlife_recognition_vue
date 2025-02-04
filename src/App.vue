<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/Navbar.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <header>
    <Navbar class=""></Navbar>
  </header>

  <RouterView />

  <Footer class="mt-100"></Footer>
</template>

<style scoped>

</style>
