<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Sidebar"
})
</script>

<template>
  <div class="h-screen bg-slate-600 w-1/6 px-6 py-2 text-base-200">
    <RouterLink to="/" class="btn btn-ghost text-xl italic -mx-4">Hobbies 24</RouterLink>
    <div class="collapse collapse-arrow bg-slate-600 my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">My Hobbies</div>
      <div class="collapse-content">
        <p>List of hobbies!</p>
      </div>
    </div>
    <div class="collapse collapse-arrow bg-slate-600 my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">Friends</div>
      <div class="collapse-content">
        <p>List of friends!</p>
      </div>
    </div>
    <div class="collapse collapse-arrow bg-slate-600 my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">Friend Requests (1)</div>
      <div class="collapse-content">
        <p>List of friend requests goes here!</p>
      </div>
    </div>
  </div>

</template>