<script lang="ts">
import {defineComponent} from 'vue'
import {Trophy, CircleHelp} from 'lucide-vue-next'

export default defineComponent({
  components: {Trophy, CircleHelp},
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
  <div class="w-full flex flex-row justify-center items-end  my-10">
    <div class="shadow-lg p-6 h-[50vh] w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between">
      <div class="rounded-full h-36  w-36 bg-orange-500">
        <div class="flex flex-row items-center justify-center h-full w-full">
          <Trophy :size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">Gabrielle</h2>
        <div class="tooltip tooltip-bottom w-full" data-tip="You both like Reading and Dancing!">
          <h3 class="cursor-pointer text-sm text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            2 Similar
            Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button class="btn self-end w-full">Add Friend</button>
    </div>
    <div class="shadow-lg p-6 h-[70vh]  w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between">
      <div class="rounded-full h-36 w-36 bg-yellow-400">
        <div class="flex flex-row items-center justify-center h-full w-full">
          <Trophy :size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">Roman</h2>
        <div class="tooltip tooltip-bottom w-full"
             data-tip="You both like Reading and Dancing and fasfsa andf gagsjkhgskj!">
          <h3 class="cursor-pointer text-sm text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            4 Similar
            Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button class="btn btn-disabled self-end w-full">Pending Request</button>
    </div>
    <div class="shadow-lg p-6 h-[60vh]  w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between">
      <div class="rounded-full h-36 w-36 bg-gray-300">
        <div class="flex flex-row items-center justify-center h-full w-full">
          <Trophy :size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">Konrad</h2>
        <div class="tooltip tooltip-bottom w-full"
             data-tip="You both like Reading and Dancing and fasfsa andf gagsjkhgskj!">
          <h3 class="cursor-pointer text-sm text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            3 Similar
            Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button class="btn self-end w-full">Add Friend</button>
    </div>
  </div>

</template>