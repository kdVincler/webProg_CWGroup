<script lang="ts">
import {defineComponent} from "vue";
import UserDisplay from "../components/UserDisplay.vue";

export default defineComponent({
  components: {UserDisplay},
  data() {
    return {
      title: "Main Page",
    }
  },
})
</script>

<template>
    <div class="h-full overflow-y-auto px-6">
      <UserDisplay v-for="i in 10" :key="i" :position="i"/>
    </div>
    <div class="join w-full flex justify-center mb-6 mt-2">
      <button class="join-item btn bg-base-100">1</button>
      <button class="join-item btn bg-base-100">2</button>
      <button class="join-item btn btn-disabled">...</button>
      <button class="join-item btn bg-base-100">99</button>
      <button class="join-item btn bg-base-100">100</button>
    </div>
</template>