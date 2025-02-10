<template>
    <nav class="bg-white">
    <div class="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
        <div class="relative flex h-16 items-center justify-between">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
            <!-- Mobile menu button-->
            <button ref="mobile_menu_ref" @click="mobile_menu = !mobile_menu" type="button" class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:ring-2 focus:ring-white focus:outline-hidden focus:ring-inset" aria-controls="mobile-menu" aria-expanded="false">
            <span class="absolute -inset-0.5"></span>
            <span class="sr-only">Open main menu</span>
            <!--
                Icon when menu is closed.

                Menu open: "hidden", Menu closed: "block"
            -->
            <svg class="block size-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
            </svg>
            <!--
                Icon when menu is open.

                Menu open: "block", Menu closed: "hidden"
            -->
            <svg class="hidden size-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true" data-slot="icon">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18 18 6M6 6l12 12" />
            </svg>
            </button>
        </div>
        <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
            <div class="flex shrink-0 items-center bg-white">
            <img class="h-15 w-auto bg-white mt-1  z-1" src="/deer_logo2.jpg" alt="Your Company">
            </div>
            <div class="hidden sm:ml-6 sm:block content-center">
            <div class="flex space-x-4">
                <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                <a href="/dashboard" class="rounded-md px-3 py-2 text-sm font-bold text-black hover:bg-black hover:text-white">Dashboard</a>
                <a href="#" class="rounded-md px-3 py-2 text-sm font-bold text-black hover:bg-black hover:text-white">Models</a>
                <a href="#" class="rounded-md px-3 py-2 text-sm font-bold text-black hover:bg-black hover:text-white">About</a>
            </div>
            </div>
        </div>
        <div class="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
            <!-- <button type="button" class="relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800 focus:outline-hidden">
            <span class="absolute -inset-1.5"></span>
            <span class="sr-only">View notifications</span>
            </button> -->

            <!-- Profile dropdown -->
            <div class="relative content-center m-auto align-center flex flex-1 items-center justify-center font-bold">
                <!-- <button type="button" class="mr-2 text-black hover:text-white border border-black hover:bg-black focus:ring-4 focus:outline-none focus:ring-black rounded-lg text-sm px-5 py-2.5 text-center">Log-in</button> -->
                <div v-if="!authStore.isAuthenticated">
                    <a href="/login" class="hover:text-gray-600 font-bold cursor-pointer mr-2 relative inline-flex items-center justify-center p-0.5 overflow-hidden text-sm text-black rounded-lg group bg-gradient-to-br from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 group-hover:from-teal-300 group-hover:to-lime-300">
                        <span class="relative px-2 text-xs sm:text-sm sm:px-5 py-2.5 transition-all ease-in duration-75 bg-white rounded-md">
                        Log-in
                        </span>
                    </a>
                    <a href="/register" type="button" class="hover:text-gray-600 cursor-pointer font-bold text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Sign-up</a>           
                </div>
                <div v-show="authStore.isAuthenticated" ref="popup_user">
                    <button @click="user_info = !user_info" type="button" class="relative flex rounded-full bg-gray-800 text-sm focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800 focus:outline-hidden" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                        <span class="absolute -inset-1.5"></span>
                        <span class="sr-only">Open user menu</span>
                        <img class="size-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt="">
                    </button>
                </div>

            <!--
                Dropdown menu, show/hide based on menu state.

                Entering: "transition ease-out duration-100"
                From: "transform opacity-0 scale-95"
                To: "transform opacity-100 scale-100"
                Leaving: "transition ease-in duration-75"
                From: "transform opacity-100 scale-100"
                To: "transform opacity-0 scale-95"
            -->
            <div v-if="authStore.isAuthenticated && user_info" class="absolute right-0 z-10 mt-38 w-48 origin-top-right rounded-md bg-white py-1 ring-1 shadow-lg ring-black/5 focus:outline-hidden" role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                <a href="#" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-0">Your Profile</a>
                <a href="#" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-1">Settings</a>
                <button @click="logout" class="block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-2">Sign out</button>
            </div>
            </div>
        </div>
        </div>
    </div>

    <!-- Mobile menu, show/hide based on menu state. -->
    <div class="sm:hidden" id="mobile-menu">
        <div class="space-y-1 px-2 pt-2 pb-3" v-show="mobile_menu">
        <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
        <a href="#" class="block rounded-md bg-gray-900 px-3 py-2 text-base font-medium text-white" aria-current="page">Dashboard</a>
        <a href="#" class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white">Models</a>
        <a href="#" class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white">Projects</a>
        <a href="#" class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white">About</a>
        </div>
    </div>
    </nav>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'
import { useAuthStore } from '../store/auth.js'
import { useRouter } from 'vue-router'





export default {
  setup() {
    const authStore = useAuthStore();
    const router = useRouter();
    const mobile_menu = ref(false);
    const user_info = ref(false);
    const popup_user = ref(null);
    const mobile_menu_ref = ref(null);


    const handleClickOutside = (event) => {
        if (popup_user.value && !popup_user.value.contains(event.target)) {
              user_info.value = false;
              console.log("Dela")
        }
        if (mobile_menu_ref.value && !mobile_menu_ref.value.contains(event.target)) {
              mobile_menu.value = false;
        }
        
    };

    onMounted(() => {
        document.addEventListener('click', handleClickOutside);
    });

    onUnmounted(() => {
      document.removeEventListener("click", handleClickOutside);
    });

    return {
      authStore, router, mobile_menu, user_info, popup_user, mobile_menu_ref
    }
  },


  methods: {
    async logout() {
      try {
        await this.authStore.logout(this.$router)
      } catch (error) {
        console.error(error)
      }
    },
  },
  async mounted() {
    await this.authStore.fetchUser()
  },
  components:{
  },

}

</script>