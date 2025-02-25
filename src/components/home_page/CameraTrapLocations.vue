<template>
    <div class="bg-white px-8">
      <div class="text-center pt-20 mb-10 text-3xl font-bold text-black max-w-[1000px] m-auto px-8">
        Data collection
        <!-- <div class="text-sm font-normal">Trained on data collected from Over 200 Camera Traps Across Slovenia</div> -->
        <div class="text-sm font-normal pt-4">
          Our system is powered by an extensive dataset gathered from over 200 strategically placed camera traps across Slovenia. 
          This diverse and comprehensive collection captures wildlife in their natural habitats, providing rich, 
          real-world data that enhances the accuracy and reliability of our models.</div>
      </div>
      <!-- <div class="text-white text-sm pt-4 text-center">
        The models were trained on 100k images, collected with the help of camera traps around Slovenia. 
        They are able to detect animals both during the day and night. 
        In total we support 10 animal classes: squirrel, wild boar, red dear, roe dear, bird, mustelid, red fox, badger, bear, chamois 
      </div> 
      <div class="text-white text-sm pt-4 text-center">
        The models were trained on a dataset of 100,000 images gathered using an extensive network of camera traps strategically placed throughout Slovenia. These advanced systems are capable of detecting wildlife activity both during the day and at night. The models currently support the identification of 10 distinct animal classes: squirrel, wild boar, red deer, roe deer, bird, mustelid, red fox, badger, bear, and chamois.
      </div>
      -->
      
      <!-- <div class="w-[90%] m-auto max-w-[1000px] bg-[url(/si-04_gray.svg)] bg-no-repeat bg-center"> -->
      <div class="relative w-full sm:w-[90%] h-[65vh] max-h-[700px] m-auto max-w-[1000px] bg-no-repeat bg-center">
        <img class="absolute top-[50%] left-[50%] -translate-x-3/7 -translate-y-1/2" src="/si-04_gray.svg"/>
        <img class=" absolute top-[50%] left-[50%] -translate-x-3/7 -translate-y-1/2 fade-in" v-fade-in src="/si-04_highlited2.png"/>
      </div>
    </div>
</template>

<script>
import { ref, onMounted, onUnmounted } from "vue";

export default {
  setup() {
    return { };
  },
  directives: {
    fadeIn: {
      mounted(el) {
        el.style.opacity = "0";
        el.style.transform = "translateY(20px)";
        el.style.transition = "opacity 2s ease-out, transform 2s ease-out";

        const handleScroll = () => {
          const rect = el.getBoundingClientRect();
          const triggerHeight = window.innerHeight * 0.9;

          if (rect.top < triggerHeight) {
            el.style.opacity = "1";
            el.style.transform = "translateY(0)";
          }
        };

        window.addEventListener("scroll", handleScroll);
        handleScroll(); 

        el.__handleScroll = handleScroll;
      },
      unmounted(el) {
        window.removeEventListener("scroll", el.__handleScroll);
      },
    },
  },
};
</script>

<style>



.fade-in {
  opacity: 0;
  transform: translateY(20px);
  /* margin: 50px auto; */
}
</style>