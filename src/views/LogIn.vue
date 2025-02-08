<template>
    <div class="sm:bg-[url(forest_bg.jpg)] bg-cover  flex items-center">
        <div class="sm:shadow-2xl p-5 sm:p-10 w-full sm:w-4/6 max-w-[600px] m-auto bg-white ">
            <form @submit.prevent="login" class="max-w-md mx-auto">
                <div class="text-center px-5 pb-5">
                    <div class="pb-5 font-bold text-3xl">
                        Log in Wildlife AI
                    </div>
                    <div>
                        By continuing, you agree to our <router-link to="/terms" class="font-bold cu">Terms of Use</router-link> and <router-link to="/privacy" class="font-bold cu">Privacy Policy</router-link>                  
                    </div>
                </div>
                <div class="mb-5">
                    <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email address</label>
                    <input v-model="email" type="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@flowbite.com" required />
                </div>
                <div class="mb-5">
                    <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                    <input v-model="password" type="password" id="password" @input="resetError" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required />
                </div>
                <div class="flex items-start mb-5">
                    <div class="flex items-center h-5">
                    <input id="remember" type="checkbox" value="" @input="resetError" class="w-4 h-4 border border-gray-300 rounded-sm bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800" />
                    </div>
                    <label for="remember" class="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300">Remember me</label>
                </div>
                <div class="w-full">
                    <button type="submit" class="m-auto text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Log in</button>
                </div>
                <div class="text-xs pt-2">
                    <p> Don't have an account? <router-link to="/register" class="font-bold cu">Sign up</router-link></p>
                </div>
            </form>
            <p v-if="error" class="text-center text-sm text-red-600 mt-10">{{ error }}</p>
        </div>
        <div class="">

        </div>
    </div>
    
</template>


<script>
import { useAuthStore } from '../store/auth'

export default {
    setup() {
      const authStore = useAuthStore()
      return {
        authStore
      }
    },
    data() {
      return {
        email: "",
        password: "",
        error: ""
      }
    },
    methods: {
      async login(){
        await this.authStore.login(this.email, this.password, this.$router)
        if (!this.authStore.isAuthenticated){
          this.error = 'Login failed. Please check your credentials.'
        }
      },
      resetError(){
        this.error = ""
      }
    }
  }
  </script>