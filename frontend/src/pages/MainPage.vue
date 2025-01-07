<script lang="ts">
import {defineComponent} from "vue";
import UserDisplay from "../components/UserDisplay.vue";
import PodiumDisplay from "@/components/PodiumDisplay.vue";

export default defineComponent({
  components: {PodiumDisplay, UserDisplay},
  data() {
    return {
      title: "Main Page",
    }
  },
})
</script>

<template>
  <div class="h-full overflow-y-auto px-6">
    <PodiumDisplay :position="1"/>
    <UserDisplay v-for="i in 7" :key="i+3" :position="i+3"/>
  </div>
  <div class="join w-full flex justify-center mb-6 mt-2">
    <button class="join-item btn bg-base-100">1</button>
        <button class="join-item btn bg-base-100">2</button>
    <button class="join-item btn btn-disabled">...</button>
        <button class="join-item btn bg-base-100">4</button>
    <button class="join-item btn bg-base-100">5</button>
  </div>
</template>