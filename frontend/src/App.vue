<script lang="ts">
import {defineComponent} from "vue";
import {RouterView} from "vue-router";
import Navbar from "@/components/Navbar.vue";
import Sidebar from "@/components/Sidebar.vue";

export default defineComponent({
  components: {Sidebar, Navbar, RouterView},
});
</script>

<template>
  <main class="flex flex-row h-screen w-screen">
    <Sidebar/>
    <div class="flex-1 h-full flex flex-col bg-base-200">
      <Navbar/>
      <RouterView/>
    </div>

  </main>

</template>