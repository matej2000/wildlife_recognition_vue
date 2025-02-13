<template>
    <Navbar></Navbar>
    <div v-show="show_dropzone" class="min-h-screen m-auto flex justify-center items-center mt-[-64px]">
      <form @submit.prevent="submitForm" action="/api" method="post" enctype="multipart/form-data" class="m-auto w-full h-fit">
        <div class="m-auto w-full h-fit">
          <div class="max-w-[800px] m-auto px-10">
            <!-- @drop.prevent="onDrop" @dragenter.prevent @dragover.prevent -->
            <div id="dropzone" ref="dropzone" @drop.prevent="onDrop" @dragenter.prevent="checkDrop" @dragover.prevent @dragleave.prevent="leaveArea" class="flex items-center justify-center w-full">
              <label for="dropzone-file" class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500">
                    <div class="flex flex-col items-center justify-center pt-5 pb-6">
                        <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                            <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                        </svg>
                        <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to upload</span> or drag and drop</p>
                        <p class="text-xs text-gray-500 dark:text-gray-400">PNG or JPG (MAX. 800x400px)</p>
                    </div>
                    <input @input="inputChange" id="dropzone-file" type="file" class="hidden" />
                </label>
            </div>
            <div class="text-center text-xs text-red-600 mt-2">
              <p>{{ error }}</p>
          </div>
          </div>
          <div v-show="loaded_file" class="max-w-[600px] m-auto px-10">

            <div class="m-auto border-2 border-gray-300 rounded-2xl mt-10 p-5">

              <div class="flex flex-row">
                <!-- <div class="absolute ml-18 mt-[-15px]">
                  <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-full text-sm p-2.5 text-center inline-flex items-center me-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                    <span class="sr-only">Close menu</span>
                    <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                  </button>
                </div> -->
                <div ref="div_preview" class="bg-white basis-1/4 hidden sm:block">
                      <img ref="preview" id="preview" class="w-[100px] h-[100px]"/>
                </div> 
                <div class="basis-[100%] sm:basis-3/4 m-auto">
                  <div class="flex flex-col">
                    <div>
                      <div class="flex flex-row justify-between items-center">
                        <p v-if="loaded_file" class="font-bold">{{ loaded_file.name.substring(loaded_file.name.length - 50) }}</p>
                        <div class="">
                          <button type="button" @click="removeFile" class="text-white cursor-pointer bg-black hover:bg-gray-500 focus:ring-4 focus:outline-none font-medium rounded-full text-sm p-2 text-center inline-flex items-center me-2 ">
                            <span class="sr-only">Close menu</span>
                            
                            <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                            </svg>
                          </button>
                        </div>
                      </div>
                      <p v-if="loaded_file" class="text-sm">{{ (loaded_file.size / 1000000).toFixed(2) + " MB"}}</p>
                    </div>
                    <div class="mt-2">
                      <div class="w-full bg-gray-200 rounded-full h-2.5 dark:bg-gray-700">
                        <div ref="bar" id="bar" class="bg-black h-2.5 rounded-full"></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="m-auto w-fit mt-10">
              <button href="/register" type="submit" class=" hover:text-gray-600 cursor-pointer font-bold text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Detect</button>           
            </div>
          </div>
        </div>
      </form>
      

    </div>

    <!-- <h1>Welcome to the home page</h1>
    <div v-if="authStore.isAuthenticated">
      <p>Hi there {{ authStore.user?.username }}!</p>
      <p>You are logged in.</p>
      <button @click="logout">Logout</button>
    </div>
    <p v-else>
      You are not logged in. <router-link to="/login">Login</router-link>
    </p> -->
    <div v-show="show_results" class="h-screen flex justify-center items-center mt-[-64px]">
      <div>
        <div class="m-auto max-w-[600px]">
          <img class="m-auto" ref="result_img"/>
        </div>
        <div class="text-center">
          <p>{{ error2 }}</p>
          <p>{{ success }}</p>
        </div>
        <div class="flex flex-row">
          <div class="m-auto w-fit mt-10">
              <button @click="loadNewImage" class=" hover:text-gray-600 cursor-pointer font-bold text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Load new image</button>           
          </div>
          <div class="m-auto w-fit mt-10">
              <a v-bind:href="image_url" download="result.png" class=" hover:text-gray-600 cursor-pointer font-bold text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Download results</a>           
          </div>
        </div>
      </div>

    </div>


</template>

<style>

.animate{
  animation: example 2s linear;
}

@keyframes example {
  0%   {width:0%}
  100% {width: 100%}
}
</style>


<script>
import {ref} from 'vue'
import Navbar from '@/components/Navbar.vue';
import { useAuthStore, getCSRFToken } from '../store/auth.js'
import { useRouter } from 'vue-router'


export default {
  setup() {
    const authStore = useAuthStore()
    const router = useRouter()
    const loaded_file = ref(null)
    const preview = ref(null)
    const bar = ref(null)
    const div_preview = ref(null)
    const dropzone = ref(null)
    const current_color = "#f9fafb"
    const error = ref("")
    const error2 = ref("")
    const success = ref("")
    const result_img = ref(null)
    const show_dropzone = ref(true)
    const show_results = ref(false)
    const image_url = ref("")

    return {
      authStore, router, loaded_file, preview, bar, div_preview, dropzone, current_color, error, error2, success, result_img, show_dropzone, show_results
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

    async submitForm(e) {
      if(this.loaded_file){
        try {
        var body = new FormData();
        body.append('file', this.loaded_file);
        const response = await fetch('http://localhost:8000/api/detect', {
          method: 'POST',
           headers: {
                    'X-CSRFToken': getCSRFToken()
                },
          body: body,
          credentials: 'include'
        })
        const data = await response
        //console.log(response)
        
        if (response.ok) {
          console.log("Ok")
          this.error = ""
          this.error2 = ""
          this.success = 'Detection successful.'
          const blob = await response.blob();
          const url = URL.createObjectURL(blob);
          this.result_img.src = url
          this.show_dropzone = false
          this.show_results = true
          this.image_url = url

        } else {
          this.error2 = data.error || 'Detection failed'
        }
      } catch (err) {
        this.error2 = 'An error occurred during detection: ' + err
        console.log(err)
      }
      }
      e.preventDefault();
    },
    checkDrop(e) {
      console.log(this.dropzone)
      //dropzone.style.backgroundColor = "#f3f4f6";
      this.current_color = "#f3f4f6";
      e.preventDefault()
    },

    leaveArea(e){
      console.log("leave")
      this.current_color = "#f9fafb";
      //dropzone.style.backgroundColor = "#f9fafb";
      e.preventDefault()
    },
    onDrop(e) {
      if (!this.isImage(e.dataTransfer.files[0].name)){
        this.error = "Please upload an image file (JPG, PNG)"
        return
      }
      this.error = ""
      this.bar.classList.remove('animate');
      void this.bar.offsetWidth;
      this.bar.classList.add('animate');
      
      this.loaded_file = e.dataTransfer.files[0];
      var reader = new FileReader();
      
      reader.onload = (event) => {  // Use arrow function to keep "this" context
        const preview = document.getElementById('preview');
        if (preview) {
          preview.src = event.target.result;
        }
      };

      reader.readAsDataURL(this.loaded_file);
    },
    inputChange(e) {
      this.bar.classList.remove('animate');
      void this.bar.offsetWidth;
      this.bar.classList.add('animate');
      
      this.loaded_file = e.target.files[0];
      var reader = new FileReader();
      
      reader.onload = (event) => {  // Use arrow function to keep "this" context
        const preview = document.getElementById('preview');
        if (preview) {
          preview.src = event.target.result;
        }
      };

      reader.readAsDataURL(this.loaded_file);
    },
    removeFile(e){
      this.loaded_file = null
      const preview = document.getElementById('preview');
      if (preview) {
        preview.src = "";
      }
      
    },
    loadNewImage(e){
      this.show_dropzone = true
      this.show_results = false
      this.loaded_file = null
    },
    getExtension(filename) {
      var parts = filename.split('.');
      return parts[parts.length - 1];
    },

    isImage(filename){
      var ext = this.getExtension(filename);
      switch (ext.toLowerCase()) {
        case 'jpg':
        case 'png':
          return true;
      }
      return false;
    }
  },
  async mounted() {
    await this.authStore.fetchUser()
    if (!this.authStore.isAuthenticated){
      this.$router.push('/login')
    }
  },
  components:{
    Navbar
  },
}
</script>