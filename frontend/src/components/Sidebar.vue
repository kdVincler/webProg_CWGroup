<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Sidebar"
})
</script>

<template>
  <div class="h-screen bg-red-400 w-1/6 px-6 py-2">
    <RouterLink to="/" class="btn btn-ghost text-xl italic -mx-4">Hobbies 24</RouterLink>
    <h2 class="text-sm font-semibold mt-4">My Hobbies</h2>
    <ul class="mt-2 gap-1 flex flex-col">
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

</template>