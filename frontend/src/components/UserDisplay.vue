<script lang="ts">
import {defineComponent} from 'vue'
import {Trophy} from 'lucide-vue-next'
import {PaginatedUser} from '../api'
import {PropType} from 'vue'

export default defineComponent({
  components: {Trophy},
  name: "UserDisplay",
  props: {
    user: {
      type: Object as PropType<PaginatedUser>,
      required: true
    },
    position: {
      type: Number,
      required: true
    },
  }
})
</script>

<template>
  <div class="w-full flex flex-row my-4 bg-base-100 card shadow-lg p-6 gap-6">
    <div class="rounded-full h-36 w-36 bg-slate-400">
      <div class="flex flex-row items-center justify-center h-full w-full">
        <span class="w-full text-center text-7xl ">{{ position }}</span>
      </div>
    </div>
    <div>
      <h2 class="text-lg font-semibold">{{user.name}}</h2>
      <h3 class="text-sm text-neutral-500 font-normal"><span class="font-bold">{{user.similar_hobbies}}</span> Similar Hobbies</h3>
    </div>
  </div>


</template>