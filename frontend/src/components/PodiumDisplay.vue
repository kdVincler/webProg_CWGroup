<script lang="ts">
import {defineComponent} from 'vue'
import {Trophy} from 'lucide-vue-next'

export default defineComponent({
  components: {Trophy},
  name: "PodiumDisplay",
  props: {
    // user: {
    //   type: Object,
    //   required: true
    // }
    position: {
      type: Number,
      required: true
    },
  }
})
</script>

<template>
  <h1 class="text-3xl font-semibold text-center">Top 3 Users Like You</h1>
  <div class="w-full flex flex-row justify-center items-end mt-[10vh] mb-[12vh]">
    <div class="shadow-lg p-6 h-[40vh] w-[14vw] bg-base-100 mx-1 flex flex-col items-center">
      <div class="rounded-full h-36 w-36 bg-orange-500">
        <div class="flex flex-row items-center justify-center h-full w-full">
          <Trophy size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">Gabrielle</h2>
        <h3 class="text-sm text-neutral-400 font-semibold text-center"><span class="font-bold">2</span> Similar Hobbies</h3>
          <div class="divider"></div>
        <ul class="mt-2 gap-1 flex flex-col list-disc font-semibold text-neutral-400">
          <li class="text-xs">
            Snowboarding
          </li>
          <li class="text-xs">
            Hiking
          </li>
        </ul>
      </div>
    </div>
    <div class="shadow-lg p-6 h-[60vh]  w-[14vw] bg-base-100 mx-1 flex flex-col items-center">
      <div class="rounded-full h-36 w-36 bg-yellow-400">
        <div class="flex flex-row items-center justify-center h-full w-full">
          <Trophy size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">Roman</h2>
        <h3 class="text-sm text-neutral-400 font-semibold text-center"><span class="font-bold">4</span> Similar Hobbies</h3>
          <div class="divider"></div>
        <ul class="mt-2 gap-1 flex flex-col list-disc font-semibold text-neutral-400">
          <li class="text-xs">
            Snowboarding
          </li>
          <li class="text-xs">
            Hiking
          </li>
          <li class="text-xs">
            Biking
          </li>
          <li class="text-xs">
            Skiing
          </li>
        </ul>
      </div>
    </div>
    <div class="shadow-lg p-6 h-[50vh]  w-[14vw] bg-base-100 mx-1 flex flex-col items-center">
      <div class="rounded-full h-36 w-36 bg-gray-300">
        <div class="flex flex-row items-center justify-center h-full w-full">
          <Trophy size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">Konrad</h2>
        <h3 class="text-sm text-neutral-400 font-semibold text-center"><span class="font-bold">3</span> Similar Hobbies</h3>
          <div class="divider"></div>
        <ul class="mt-2 gap-1 flex flex-col list-disc font-semibold text-neutral-400">
          <li class="text-xs">
            Snowboarding
          </li>
          <li class="text-xs">
            Hiking
          </li>
          <li class="text-xs">
            Biking
          </li>
        </ul>
      </div>
    </div>
  </div>

</template>