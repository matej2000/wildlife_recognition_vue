<template>
  <div>
    <Navbar class="bg-white border-b-1 border-gray-300"></Navbar>
    <div class="relative lg:flex lg:flex-row min-h-screen">
      <!-- Start side menu -->
      <!-- transition-transform -translate-x-full sm:translate-x-0-->
      <div v-show="showSettings"
        class="w-full flex flex-row absolute lg:w-full h-full lg:h-auto lg:static lg:flex-none lg:basis-70 z-30">
        <div class="h-full bg-gray-50 basis-70  border-r-1 border-gray-300 px-3 ">
          <div class="flex flex-row justify-between pt-2 border-b pb-1 border-gray-300">
            <div class="text-2xl font-bold">
              Settings
            </div>
            <button @click="showSettings = false"
              class="w-fit h-fit text-white cursor-pointer bg-gray-100 border-1 border-gray-100 hover:bg-gray-200 focus:ring-4 focus:outline-none font-medium rounded-full text-sm p-1 text-center inline-flex items-center ">
              <span class="sr-only">Close menu</span>
              <svg class="h-5 w-5 text-black" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>

          </div>
          <div>
            <p class="mt-5 ml-2 font-bold">Select classes to detect:</p>
            <div class="grid grid-cols-2 gap-2 justify-center mt-3">
              <div v-for="(label, index) in labels" :key="index" class="flex-1 text-sm">
                <div v-if="selected_labels[index]" @click="selected_labels[index] = false"
                  class="cursor-pointer px-4 py-2 bg-blue-200 rounded-xl flex flex-row items-center gap-3 justify-between">
                  <p>{{ label }}</p>
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                    stroke="currentColor" class="size-4">
                    <path stroke-linecap="round" stroke-linejoin="round" d="m4.5 12.75 6 6 9-13.5" />
                  </svg>
                </div>
                <div v-else @click="selected_labels[index] = true"
                  class="cursor-pointer text-center hover:bg-gray-300 m-auto px-4 py-2 bg-gray-200 rounded-xl flex flex-row items-center gap-3 justify-center">
                  <p>{{ label }}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="w-full">
            <p class="mt-10 ml-2 font-bold">Maximum number of detections:</p>
            <div class="flex flex-row justify-center gap-5 items-center mt-2">
              <input id="default-range" type="range" v-model="maxDetections" min="1" max="100"
                class="w-[70%]  h-2 bg-gray-300 rounded-lg appearance-none cursor-pointer">
              <input type="number" v-model="maxDetections" min="1" max="100" class="w-[50px]">
            </div>
          </div>
          <div>
            <p class="mt-10 ml-2 font-bold">Confidence threshold:</p>
            <div class="flex flex-row justify-center gap-5 items-center mt-2">
              <input id="default-range" type="range" v-model="confThreshold" min="0" max="1" step="0.1"
                class="w-[70%]  h-2 bg-gray-300 rounded-lg appearance-none cursor-pointer">
              <input type="number" v-model="confThreshold" step="0.1" min="0" max="1" class="w-[50px]">
            </div>
          </div>
        </div>
        <div id="overlay" @click="showSettings = false"
          class="opacity-30 bg-black flex-grow z-30 lg:opacity-0 lg:z-0 lg:w-0">
        </div>
      </div>
      <!-- END side menu -->
      <div class="bg-gray-50 flex-grow">
        <div class="relative flex flex-row pt-10 gap-2 ml-10">
          <button @click="showSettings = !showSettings"
            class="bg-gray-50 p-2 rounded-xl w-fit cursor-pointer hover:bg-gray-200">
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="size-6">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M10.5 6h9.75M10.5 6a1.5 1.5 0 1 1-3 0m3 0a1.5 1.5 0 1 0-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 0 1-3 0m3 0a1.5 1.5 0 0 0-3 0m-9.75 0h9.75" />
            </svg>
          </button>
          <button @click="show_dropMenu = !show_dropMenu"
            class="cursor-pointer text-xl flex flex-row px-4 py-2 rounded-xl hover:bg-gray-200">
            <p class="mr-2 font-bold">{{ selectedModel }}</p>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor" class="size-5 m-auto stroke-4 text-gray-400">
              <path stroke-linecap="round" stroke-linejoin="round" d="m19.5 8.25-7.5 7.5-7.5-7.5" />
            </svg>
          </button>
          <div v-show="show_dropMenu"
            class="absolute text-lg border-1 mt-3 px-2 py-2 top-20 bg-gray-50 flex flex-col w-[300px] text-start shadow-2xl rounded-xl z-20">
            <button @click="selectedModel = 'Weakly large'; show_dropMenu = false"
              class="cursor-pointer text-start hover:bg-gray-200 py-2 px-4 rounded-xl" id="weakly_large">
              <div class="flex flex-row gap-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                  stroke="currentColor" class="size-6">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="m21 7.5-2.25-1.313M21 7.5v2.25m0-2.25-2.25 1.313M3 7.5l2.25-1.313M3 7.5l2.25 1.313M3 7.5v2.25m9 3 2.25-1.313M12 12.75l-2.25-1.313M12 12.75V15m0 6.75 2.25-1.313M12 21.75V19.5m0 2.25-2.25-1.313m0-16.875L12 2.25l2.25 1.313M21 14.25v2.25l-2.25 1.313m-13.5 0L3 16.5v-2.25" />
                </svg>
                <p>Weakly large</p>
              </div>
            </button>
            <button @click="selectedModel = 'Point small'; show_dropMenu = false"
              class="cursor-pointer text-start hover:bg-gray-200 px-4 py-2 rounded-xl" id="point_small">
              <div class="flex flex-row gap-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                  stroke="currentColor" class="size-6">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="m3.75 13.5 10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75Z" />
                </svg>
                <p>Point small</p>
              </div>
            </button>
            <button @click="selectedModel = 'Point large'; show_dropMenu = false"
              class="cursor-pointer text-start hover:bg-gray-200 px-4 py-2 rounded-xl justify-center items-center"
              id="point_large">
              <div class="flex flex-row gap-3">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                  stroke="currentColor" class="size-6">
                  <path stroke-linecap="round" stroke-linejoin="round"
                    d="M9.813 15.904 9 18.75l-.813-2.846a4.5 4.5 0 0 0-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 0 0 3.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 0 0 3.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 0 0-3.09 3.09ZM18.259 8.715 18 9.75l-.259-1.035a3.375 3.375 0 0 0-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 0 0 2.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 0 0 2.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 0 0-2.456 2.456ZM16.894 20.567 16.5 21.75l-.394-1.183a2.25 2.25 0 0 0-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 0 0 1.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 0 0 1.423 1.423l1.183.394-1.183.394a2.25 2.25 0 0 0-1.423 1.423Z" />
                </svg>
                <p>Point large</p>
              </div>
            </button>
          </div>
        </div>

        <div v-show="show_dropMenu" @click="show_dropMenu = false" class="left-0 top-0 absolute w-screen h-screen z-10">
        </div>
        <div v-show="show_dropzone" class="min-h-screen m-auto flex justify-center sm:mt-[-64px] items-center">
          <form @submit.prevent="submitForm" action="/api" method="post" enctype="multipart/form-data"
            class="m-auto w-full h-fit">
            <div class="m-auto w-full h-fit">
              <div class="max-w-[800px] m-auto px-10">
                <!-- @drop.prevent="onDrop" @dragenter.prevent @dragover.prevent -->
                <div class="text-center mb-10 text-3xl font-bold">
                  <h1>Select and upload an image for animal detection</h1>
                </div>
                <div id="dropzone" ref="dropzone" @drop.prevent="onDrop" @dragenter.prevent="checkDrop"
                  @dragover.prevent @dragleave.prevent="leaveArea" class="flex items-center justify-center w-full">
                  <label for="dropzone-file"
                    class="flex flex-col items-center justify-center w-full h-64 border-2 border-black border-dashed rounded-lg cursor-pointer bg-white dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500">
                    <div class="flex flex-col items-center justify-center pt-5 pb-6">
                      <svg class="w-8 h-8 mb-4 text-gray-500 dark:text-gray-400" aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                          d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2" />
                      </svg>
                      <p class="mb-2 text-sm text-gray-500 dark:text-gray-400"><span class="font-semibold">Click to
                          upload</span> or drag and drop</p>
                      <p class="text-xs text-gray-500 dark:text-gray-400">PNG or JPG (MAX. 800x400px)</p>
                    </div>
                    <input @change="inputChange" @input="inputChange" id="dropzone-file" type="file" class="hidden" />
                  </label>
                </div>
                <div class="text-center text-xs text-red-600 mt-2">
                  <p>{{ error }}</p>
                </div>
              </div>
              <!-- Start of loaded file preview -->
              <div v-show="loaded_file" class="max-w-[600px] m-auto px-10 pb-10">

                <div class="m-auto border-1 border-black bg-white rounded-2xl mt-10 p-5">

                  <div class="flex flex-row">
                    <!-- <div class="absolute ml-18 mt-[-15px]">
                      <button type="button" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-full text-sm p-2.5 text-center inline-flex items-center me-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                        <span class="sr-only">Close menu</span>
                        <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                      </button>
                    </div> -->
                    <div ref="div_preview" class="basis-1/4 hidden sm:block">
                      <img ref="preview" id="preview" class="w-[100px] h-[100px]" />
                    </div>
                    <div class="basis-[100%] sm:basis-3/4 m-auto">
                      <div class="flex flex-col">
                        <div>
                          <div class="flex flex-row justify-between items-center">
                            <p v-if="loaded_file" class="font-bold">{{
                              loaded_file.name.substring(loaded_file.name.length - 50) }}</p>
                            <div class="">
                              <button type="button" @click="removeFile"
                                class="text-white cursor-pointer bg-black hover:bg-gray-500 focus:ring-4 focus:outline-none font-medium rounded-full text-sm p-2 text-center inline-flex items-center me-2 ">
                                <span class="sr-only">Close menu</span>

                                <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"
                                  stroke="currentColor" aria-hidden="true">
                                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                    d="M6 18L18 6M6 6l12 12" />
                                </svg>
                              </button>
                            </div>
                          </div>
                          <p v-if="loaded_file" class="text-sm">{{ (loaded_file.size / 1000000).toFixed(2) + " MB" }}
                          </p>
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
                  <button type="submit"
                    class="cursor-pointer border-2 border-black px-4 py-3 rounded-md text-white bg-black font-bold hover:bg-white hover:text-black">Detect</button>

                  <!-- <button type="submit" class=" hover:text-gray-600 cursor-pointer font-bold text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Detect</button>            -->
                </div>
              </div>
              <!-- End of loaded file preview -->
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
            <div class="m-auto max-w-[600px] border-2 border-dashed rounded-xl">
              <img class="m-auto" ref="result_img" />
            </div>
            <div class="text-center mt-3">
              <p>{{ error2 }}</p>
              <p>{{ success }}</p>
            </div>
            <div class="flex flex-row mt-10">
              <div class="m-auto w-fit">
                <button @click="loadNewImage"
                  class="cursor-pointer border-2 border-black px-4 py-3 rounded-md text-white bg-black font-bold hover:bg-white hover:text-black">
                  <div class="flex flex-row gap-3">
                    <p>New image</p>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                      stroke="currentColor" class="size-6">
                      <path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15" />
                    </svg>
                  </div>
                </button>
                <!-- <button @click="loadNewImage" class=" hover:text-gray-600 cursor-pointer font-bold text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Load new image</button>            -->
              </div>
              <div class="m-auto w-fit ">
                <a v-bind:href="image_url" download="result.png"
                  class="flex cursor-pointer border-2 border-black px-4 py-3 rounded-md text-white bg-black font-bold hover:bg-white hover:text-black">
                  <div class="flex flex-row gap-3">
                    <p>Download</p>
                    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
                      stroke="currentColor" class="size-6">
                      <path stroke-linecap="round" stroke-linejoin="round"
                        d="M3 16.5v2.25A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75V16.5M16.5 12 12 16.5m0 0L7.5 12m4.5 4.5V3" />
                    </svg>

                  </div>
                </a>
                <!-- <a v-bind:href="image_url" download="result.png" class=" hover:text-gray-600 cursor-pointer font-bold text-black bg-gradient-to-r from-teal-200 to-lime-200 hover:from-teal-100 hover:to-lime-100 rounded-lg text-xs sm:text-sm px-2 sm:px-5 py-2.5 text-center ">Download results</a>            -->
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>


</template>

<style>
.animate {
  animation: example 2s linear;
}

@keyframes example {
  0% {
    width: 0%
  }

  100% {
    width: 100%
  }
}
</style>


<script>
import { ref } from 'vue'
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
    const show_dropMenu = ref(false)
    const selectedModel = ref("Point small")
    const labels = [
      "Badger",
      "Bear",
      "Birds",
      "Chamois",
      "Mustelid",
      "Red deer",
      "Red fox",
      "Roe deer",
      "Squirrel",
      "Wild boar"
    ];
    const selected_labels = ref([true, true, true, true, true, true, true, true, true, true])
    const maxDetections = ref("50")
    const confThreshold = ref("0.5")
    const showSettings = ref(window.innerWidth >= 1024);

    return {
      authStore, router, loaded_file, preview, bar, div_preview,
      dropzone, current_color, error, error2, success, result_img, show_dropzone,
      show_results, show_dropMenu, selectedModel, labels, maxDetections, confThreshold,
      showSettings, selected_labels
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
      e.preventDefault();

      if (this.loaded_file) {
        try {
          const body = new FormData();
          body.append('file', this.loaded_file);

          const response = await fetch('/api/detect/megadetector/', {
            method: 'POST',
            headers: {
              'X-CSRFToken': getCSRFToken()
            },
            body: body,
            credentials: 'include'
          });

          const data = await response.json();

          if (response.ok) {
            this.error = "";
            this.error2 = "";
            this.success = 'Detection successful.';

            const url = `data:image/jpeg;base64,${data.annotated_image}`;

            this.result_img.src = url;
            this.show_dropzone = false;
            this.show_results = true;
            this.image_url = url;

          } else {
            this.error2 = data.error || 'Detection failed';
          }

        } catch (err) {
          this.error2 = 'An error occurred during detection: ' + err;
          console.log(err);
        }
      }
    },
    checkDrop(e) {
      console.log(this.dropzone)
      //dropzone.style.backgroundColor = "#f3f4f6";
      this.current_color = "#f3f4f6";
      e.preventDefault()
    },

    leaveArea(e) {
      console.log("leave")
      this.current_color = "#f9fafb";
      //dropzone.style.backgroundColor = "#f9fafb";
      e.preventDefault()
    },
    onDrop(e) {
      if (!this.isImage(e.dataTransfer.files[0].name)) {
        this.error = 'Please upload an image file (JPG, PNG)'
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
    removeFile(e) {
      this.loaded_file = null
      const preview = document.getElementById('preview');
      if (preview) {
        preview.src = "";
      }

    },
    loadNewImage(e) {
      this.show_dropzone = true
      this.show_results = false
      this.loaded_file = null
    },
    getExtension(filename) {
      var parts = filename.split('.');
      return parts[parts.length - 1];
    },

    isImage(filename) {
      var ext = this.getExtension(filename);
      switch (ext.toLowerCase()) {
        case 'jpg':
        case 'png':
          return true;
      }
      return false;
    },
  },
  async mounted() {
    await this.authStore.fetchUser()
    if (!this.authStore.isAuthenticated) {
      this.$router.push('/login')
    }
  },
  components: {
    Navbar
  },
}
</script>