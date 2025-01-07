<script lang="ts">
import {defineComponent} from 'vue'
import {Trophy} from 'lucide-vue-next'

export default defineComponent({
  components: {Trophy},
  name: "UserDisplay",
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
  <div class="w-full flex flex-row my-4 bg-base-100 card shadow-lg p-6 gap-6">
    <div v-if="position == 1" class="rounded-full h-36 w-36 bg-yellow-400">
      <div class="flex flex-row items-center justify-center h-full w-full">
        <Trophy size="64" />
      </div>
    </div>
    <div v-else-if="position === 2" class="rounded-full h-36 w-36 bg-gray-300">
      <div class="flex flex-row items-center justify-center h-full w-full">
        <Trophy size="64" />
      </div>
    </div>
    <div v-else-if="position === 3" class="rounded-full h-36 w-36 bg-orange-400">
      <div class="flex flex-row items-center justify-center h-full w-full">
        <Trophy size="64" />
      </div>
    </div>
    <div v-else class="rounded-full h-36 w-36 bg-red-400">
      <div class="flex flex-row items-center justify-center h-full w-full">
        <span class="w-full text-center text-5xl font-light italic">{{ position }}th</span>
      </div>
    </div>
    <div>
      <h2 class="text-lg font-semibold">Roman Pretty</h2>
      <h3 class="text-sm text-neutral-500 font-normal"><span class="font-bold">4</span> Similar Hobbies</h3>
    </div>
  </div>


</template>