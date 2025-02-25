<template>
    <div class="px-8 pb-20 pt-20 bg-gray-300">
      <div class="text-3xl text-center font-bold mb-10 ">
        Available models
      </div>
      <div class="flex flex-3 flex-row flex-wrap w-full justify-center gap-10">
        <div class="shadow-2xl p-10 text-center w-[300px] bg-white rounded-2xl">
          <div class="mb-3 text-xl font-bold">
            Weakly large
          </div>
          <div>
              <img src="/model_logo.png"/>
            </div>
          <div class="mb-3">
            Backbone: Resnet 50
          </div>
          <div class="mb-20">
            <div class="mb-1 ">Performance</div>
            <div class="w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700">
              <div class="bg-blue-300 h-2.5 rounded-full dark:bg-blue-500" style="width: 30%"></div>
            </div>
          </div>
          <div class="">
            <button type="button" class="hover:text-black border-2 border-black cursor-pointer font-bold text-white bg-black hover:bg-white rounded-lg text-sm px-5 py-2.5 text-center">Try for free</button> 
          </div>
        </div>
        <div class="p-10 text-center w-[300px] rounded-2xl shadow-2xl bg-white">
          <div class="mb-3 text-xl font-bold">
            Point small
          </div>
          <div>
              <img src="/model_logo_small.png"/>
            </div>
          <div class="mb-3">
            Backbone: Resnet 18
          </div>
          <div class="mb-20">
            <div class="mb-1 ">Performance</div>
            <div class="w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700">
              <div class="bg-blue-300 h-2.5 rounded-full dark:bg-blue-500" style="width: 40%"></div>
            </div>
          </div>
          <div class="">
            <button type="button" class="hover:text-black border-2 border-black cursor-pointer font-bold text-white bg-black hover:bg-white rounded-lg text-sm px-5 py-2.5 text-center">Try for free</button> 
          </div>
        </div>
        <div class="p-10 text-center w-[300px] rounded-2xl shadow-2xl bg-white">
          <div class="mb-3 text-xl font-bold">
            Point large
          </div>
          <div>
              <img src="/model_logo.png"/>
            </div>
          <div class="mb-3">
            Backbone: Resnet 50
          </div>
          <div class="mb-20">
            <div class="mb-1 ">Performance</div>
            <div class="w-full bg-gray-200 rounded-full h-2.5 mb-4 dark:bg-gray-700">
              <div class="bg-blue-300 h-2.5 rounded-full dark:bg-blue-500" style="width: 90%"></div>
            </div>
          </div>
          <div class="">
            <button type="button" class="hover:text-black border-2 border-black cursor-pointer font-bold text-white bg-black hover:bg-white rounded-lg text-sm px-5 py-2.5 text-center">Try for free</button> 
          </div>
        </div>
      </div>
    </div>
</template>