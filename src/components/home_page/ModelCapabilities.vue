<template>
    <div class="pt-20">
      <div class="px-8 max-w-[1000px] m-auto">
        <div class="text-center text-3xl font-bold pb-4">
          Model Capabilities
        </div>
        <div class="text-center">
          <p>Our models employ a state-of-the-art technique that enables them to leverage weakly supervised data effectively. 
            By refining this approach, we achieved superior results, surpassing the original model that first introduced the technique.
          </p>
        </div>
      </div>
      <div class="px-8 pt-15 pb-16 overflow-x-auto max-w-[1500px] m-auto">
        <table class="w-full text-sm text-center whitespace-nowrap">
          <thead class="uppercase border-b border-gray-200">
            <tr>
              <th class="px-2 pt-2 pb-1">Benchmark (Metric)</th>
              <th class="px-2 pt-1.5 pb-3">Weakly small</th>
              <th class="px-2 pt-1.5 pb-3">Weakly large</th>
              <th class="px-2 pt-1.5 pb-3">Point small</th>
              <th class="bg-blue-200 rounded-t-xl">Point large</th>
              <th class="px-2 pt-1.5 pb-3">DeepFauna</th>
            </tr>
          </thead>
          <tbody>
            <tr >
              <td class="px-2 pt-2 pb-1">Training type</td>
              <td class="px-2 pt-1.5 pb-3">Weakly supervised</td>
              <td class="px-2 pt-1.5 pb-3">Weakly supervised</td>
              <td class="px-2 pt-1.5 pb-3">Point supervised</td>
              <td class="bg-blue-200">Point supervised</td>
              <td class="px-2 pt-1.5 pb-3">Supervised</td>
            </tr>
            <tr >
              <td class="px-2 pt-2 pb-1">Backbone</td>
              <td class="px-2 pt-1.5 pb-3">ResNet18</td>
              <td class="px-2 pt-1.5 pb-3">ResNet50</td>
              <td class="px-2 pt-1.5 pb-3">ResNet18</td>
              <td class="bg-blue-200">ResNet50</td>
              <td class="px-2 pt-1.5 pb-3">Supervised</td>
            </tr>
            <tr>
              <td class="px-2 pt-2 pb-1">Architecture</td>
              <td class="px-2 pt-1.5 pb-3">RT-DETR</td>
              <td class="px-2 pt-1.5 pb-3">RT-DETR</td>
              <td class="px-2 pt-1.5 pb-3">RT-DETR</td>
              <td class="bg-blue-200">RT-DETR</td>
              <td class="px-2 pt-1.5 pb-3">Faster RCNN</td>
            </tr>
            
            <tr>
              <td class="px-2 pt-2 pb-1"># Total Params</td>
              <td class="px-2 pt-1.5 pb-3">20M</td>
              <td class="px-2 pt-1.5 pb-3">40M</td>
              <td class="px-2 pt-1.5 pb-3">20M</td>
              <td class="bg-blue-200">40M</td>
              <td class="px-2 pt-1.5 pb-3">?</td>
            </tr>
            <tr class="border-t border-gray-200">
              <td class="px-2 pt-2 pb-1">mAP</td>
              <td class="px-2 pt-1.5 pb-3"></td>
              <td class="px-2 pt-1.5 pb-3"></td>
              <td class="px-2 pt-1.5 pb-3">0.26</td>
              <td class="bg-blue-200">0.3</td>
              <td class="px-2 pt-1.5 pb-3"></td>
            </tr>
            <tr>
              <td class="px-2 pt-2 pb-1">mAP_0.5</td>
              <td class="px-2 pt-1.5 pb-3"></td>
              <td class="px-2 pt-1.5 pb-3">0.42</td>
              <td class="px-2 pt-1.5 pb-3">0.38</td>
              <td class="bg-blue-200">0.51</td>
              <td class="px-2 pt-1.5 pb-3">0.6</td>
            </tr>
            <tr>
              <td class="px-2 pt-2 pb-1">AR_1</td>
              <td class="px-2 pt-1.5 pb-3">0.3</td>
              <td class="px-2 pt-1.5 pb-3">0.4</td>
              <td class="px-2 pt-1.5 pb-3"></td>
              <td class="bg-blue-200"></td>
              <td class="px-2 pt-1.5 pb-3"></td>
            </tr>
            <tr>
              <td class="px-2 pt-2 pb-1">AR_100</td>
              <td class="px-2 pt-1.5 pb-3">0.3</td>
              <td class="px-2 pt-1.5 pb-3">0.4</td>
              <td class="px-2 pt-1.5 pb-3"></td>
              <td class="bg-blue-200 rounded-b-xl"></td>
              <td class="px-2 pt-1.5 pb-3"></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
</template>