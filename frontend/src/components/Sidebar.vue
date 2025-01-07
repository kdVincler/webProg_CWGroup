<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Sidebar"
})
</script>

<template>
  <div class="h-screen bg-slate-600 w-1/6 px-6 py-2 text-base-200">
    <RouterLink to="/" class="btn btn-ghost text-xl italic -mx-4">Hobbies 24</RouterLink>
  </div>

</template>