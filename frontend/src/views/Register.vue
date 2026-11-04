<template>
  <div class="sm:bg-[url(/forest_bg.jpg)] bg-cover flex items-center">
    <div class="sm:shadow-2xl p-5 sm:p-10 w-full sm:w-4/6 max-w-[600px] m-auto bg-white ">
      <form @submit.prevent="register" class="max-w-md mx-auto">
        <div class="text-center px-5 pb-5">
          <div class="pb-5 font-bold text-3xl">
            Wildlife AI
          </div>
          <div>
            Sign up for free to use our state of the art wildlife recognition AI.
          </div>
        </div>
        <div class="grid md:grid-cols-2 md:gap-6 px-5">
          <div class="relative z-0 w-full mb-5 group">
            <label for="floating_first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">First
              name</label>
            <input v-model="first_name" type="text" name="floating_first_name" id="floating_first_name"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 sm:p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Enter your name" required />
          </div>
          <div class="relative z-0 w-full mb-5 group">
            <label for="floating_last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Last
              name</label>
            <input v-model="last_name" type="text" name="floating_last_name" id="floating_last_name"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 sm:p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
              placeholder="Enter your last name" required />
          </div>
        </div>
        <div class="relative z-0 w-full mb-5 group px-5">
          <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Email address</label>
          <input v-model="email" type="email" id="email"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 sm:p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            placeholder="example@gmail.com" required />
        </div>
        <div class="relative z-0 w-full mb-5 group px-5">
          <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
          <input placeholder="**********" v-model="password" type="password" id="password" @input="resetError"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 sm:p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required />
        </div>
        <div class="relative z-0 w-full mb-5 group px-5">
          <label for="confirm_password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm
            password</label>
          <input placeholder="**********" v-model="confirm_password" type="password" id="confirm_password"
            @input="resetError"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2 sm:p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
            required />
        </div>
        <div class="px-5">
          <button type="submit"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
        </div>
        <div class="text-xs pt-2 px-5">
          <p> Have an account? <router-link to="/login" class="font-bold cu">Log in</router-link></p>
        </div>
        <p v-if="error" class="text-center text-sm text-red-600 mt-10">{{ error }}</p>
      </form>
    </div>
  </div>

</template>


<script>
import { getCSRFToken } from '../store/auth'

export default {
  data() {
    return {
      email: '',
      password: '',
      confirm_password: '',
      first_name: '',
      last_name: '',
      error: '',
      success: ''
    }
  },
  methods: {
    async register() {
      if (this.password != this.confirm_password) {
        this.error = 'Passwords do not match'
        return
      }
      try {
        const response = await fetch('/api/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken()
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
            first_name: this.first_name,
            last_name: this.last_name
          }),
          credentials: 'include'
        })
        const data = await response.json()
        if (response.ok) {
          this.success = 'Registration successful! Please log in.'
          setTimeout(() => {
            this.$router.push('/login')
          }, 1000)
        } else {
          this.error = data.error || 'Registration failed'
        }
      } catch (err) {
        this.error = 'An error occurred during registration: ' + err
      }
    }
  }
}
</script>