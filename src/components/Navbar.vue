<template>
    <nav class="">
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
            <div class="flex shrink-0 items-center">
            <a href="/">
                <img class="cursor-pointer h-15 w-auto mt-1 z-1" src="/deer_logo2_transparent.png" alt="Your Company">
            </a>
            </div>
            <div class="hidden sm:ml-6 sm:block content-center">
            <div class="flex space-x-4">
                <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                <a href="/dashboard" class="rounded-md px-3 py-2 text-sm font-bold text-black hover:bg-black hover:text-white">Dashboard</a>
                <a href="/#models" class="rounded-md px-3 py-2 text-sm font-bold text-black hover:bg-black hover:text-white">Models</a>
                <a href="/#capabilities" class="rounded-md px-3 py-2 text-sm font-bold text-black hover:bg-black hover:text-white">About</a>
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
                    <!-- <a href="/login" class="hover:text-gray-600 font-bold cursor-pointer mr-2 relative inline-flex items-center justify-center p-0.5 overflow-hidden text-sm text-black rounded-lg group bg-gradient-to-br from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 group-hover:from-teal-300 group-hover:to-lime-300">
                        <span class="relative px-2 text-xs sm:text-sm sm:px-5 py-2.5 transition-all ease-in duration-75 bg-white rounded-md">
                        Log-in
                        </span>
                    </a> -->
                    <a href="/login" type="button" class="hover:bg-white hover:text-black border-black mr-2 border-2 cursor-pointer font-bold text-white bg-black rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Log-in</a>           
                    <!-- <a href="/register" type="button" class="hover:text-gray-600 cursor-pointer font-bold text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Sign-up</a>            -->
                    <a href="/register" type="button" class="hover:bg-white border-2 border-black cursor-pointer font-bold text-black bg-blue-200 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Sign-up</a>           
                </div>
                <div v-show="authStore.isAuthenticated" ref="popup_user">
                    <button @click="user_info = !user_info" type="button" class="size-7 overflow-hidden border-2 cursor-pointer relative flex rounded-full bg-gray-800 text-sm focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800 focus:outline-hidden" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                        <span class="absolute -inset-1.5"></span>
                        <span class="sr-only">Open user menu</span>
                        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-8 bg-gray-300 fill-white">
                            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0ZM4.501 20.118a7.5 7.5 0 0 1 14.998 0A17.933 17.933 0 0 1 12 21.75c-2.676 0-5.216-.584-7.499-1.632Z" />
                        </svg>

                        <!-- <img class="size-8 rounded-full" src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80" alt=""> -->
                    </button>
                </div>

            <div v-if="authStore.isAuthenticated && user_info" class="absolute right-0 z-50 px-1 mt-38 w-48 origin-top-right rounded-xl bg-white py-1 ring-1 shadow-lg ring-black/5 focus:outline-hidden" role="menu" aria-orientation="vertical" aria-labelledby="user-menu-button" tabindex="-1">
                <a href="#" class="w-full hover:bg-gray-100 rounded-xl block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-0">Your Profile</a>
                <a href="#" class="w-full hover:bg-gray-100 rounded-xl block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-1">Settings</a>
                <button @click="logout" class="rounded-xl text-left cursor-pointer hover:bg-gray-100 w-full block px-4 py-2 text-sm text-gray-700" role="menuitem" tabindex="-1" id="user-menu-item-2">Sign out</button>
            </div>
            </div>
        </div>
        </div>
    </div>
    <!-- <div v-if="authStore.isAuthenticated && user_info" @click="user_info = false" class="fixed w-screen h-screen top-0 left-0 z-9"></div> -->
    <div v-if="authStore.isAuthenticated && user_info" @click="user_info = false" class="absolute w-screen h-screen top-0 left-0 z-40"></div>


    <!-- Mobile menu, show/hide based on menu state. -->
    <!-- <div class="absolute w-screen top-[64px] left-0 z-50" id="mobile-menu">
        <div class="space-y-1 px-2 pt-2 pb-3 bg-white" v-show="mobile_menu">
            <a href="#" class="block rounded-md bg-gray-900 px-3 py-2 text-base font-medium text-white" aria-current="page">Dashboard</a>
            <a href="/#models" class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white">Models</a>        
            <a href="/#capabilities" class="block rounded-md px-3 py-2 text-base font-medium text-gray-300 hover:bg-gray-700 hover:text-white">About</a>
        </div>
    </div> -->
    <div v-show="mobile_menu" class="flex flex-row z-60 w-screen h-screen absolute top-0 left-0">
        <div class="flex flex-col basis-70 bg-white px-2">
            <div class="flex flex-row justify-between items-center mt-2 px-3 border-b-1 border-gray-300 pb-1">
                <div>
                    <a href="/">
                        <img class="cursor-pointer h-10 w-auto mt-1 z-1" src="/deer_logo2_transparent.png" alt="Your Company">
                    </a>
                </div>
                <div>
                    <button @click="mobile_menu = false" class="w-fit h-fit text-white cursor-pointer bg-white border-gray-100 hover:bg-gray-200 focus:ring-4 focus:outline-none font-medium rounded-full text-sm p-1 text-center inline-flex items-center ">
                        <span class="sr-only">Close menu</span>
                        <svg class="h-5 w-5 text-black" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
            </div>
            <div class="items-center m-auto w-full text-xl text-center">
                <a @click="mobile_menu = false" href="/dashboard" class="hover:bg-black hover:text-white mb-5 block rounded-md py-2 font-bold" aria-current="page">Dashboard</a>
                <a @click="mobile_menu = false" href="/#models" class="hover:bg-black hover:text-white mb-5 block rounded-md py-2 font-bold">Models</a>
                <a @click="mobile_menu = false" href="/#capabilities" class="hover:bg-black hover:text-white mb-5 block rounded-md py-2 font-bold">About</a>
                <a @click="mobile_menu = false" href="/register" class="hover:bg-black hover:text-white mb-5 block rounded-md py-2 font-bold">Sign-up</a>        
                <a @click="mobile_menu = false" href="/login" class="hover:bg-black hover:text-white block rounded-md py-2 font-bold">Log-in</a>        

            </div>
            <div class="flex flex-row justify-between text-md ml-2 pb-3 cursor-pointer">
                <div class="flex flex-row ml-2">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M7.217 10.907a2.25 2.25 0 1 0 0 2.186m0-2.186c.18.324.283.696.283 1.093s-.103.77-.283 1.093m0-2.186 9.566-5.314m-9.566 7.5 9.566 5.314m0 0a2.25 2.25 0 1 0 3.935 2.186 2.25 2.25 0 0 0-3.935-2.186Zm0-12.814a2.25 2.25 0 1 0 3.933-2.185 2.25 2.25 0 0 0-3.933 2.185Z" />
                    </svg>
                    <p>Share</p>
                </div>
                <div class="flex flex-row mr-2 cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-5 mr-2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 1 0-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 0 0 2.25-2.25v-6.75a2.25 2.25 0 0 0-2.25-2.25H6.75a2.25 2.25 0 0 0-2.25 2.25v6.75a2.25 2.25 0 0 0 2.25 2.25Z" />
                    </svg>
                    <p>Privacy</p>
                </div>
            </div>
        </div>
        <div @click="mobile_menu = false" class="flex-grow bg-black opacity-30"></div>

    </div>
    </nav>
</template>

<script>
import { ref, onMounted, onUnmounted, watch } from 'vue'
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

    const disableScroll = () => {
      document.body.style.overflow = "hidden";
    };

    const enableScroll = () => {
      document.body.style.overflow = "";
    };

    watch(mobile_menu, (newVal) => {
      if (newVal) {
        disableScroll();
      } else {
        enableScroll();
      }
    });

    // const handleClickOutside = (event) => {
    //     if (popup_user.value && !popup_user.value.contains(event.target)) {
    //           user_info.value = false;
    //     }
    //     if (mobile_menu_ref.value && !mobile_menu_ref.value.contains(event.target)) {
    //           mobile_menu.value = false;
    //     }
        
    // };

    // onMounted(() => {
    //     document.addEventListener('click', handleClickOutside);
    // });

    // onUnmounted(() => {
    //   document.removeEventListener("click", handleClickOutside);
    // });

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