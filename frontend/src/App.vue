<template>
  <div class="navbar bg-base-200">
    <div class="flex-1">
      <a class="btn btn-ghost text-xl">Hobby App</a>
    </div>
    <div class="flex-none gap-2">
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div class="w-10 rounded-full bg-red-400 ">
            <!--TODO: Add User Initials or profile picture-->
            <div class="flex flex-row items-center justify-center h-full w-full">
              <span class="w-full text-center">RP</span>
            </div>

          </div>
        </div>
        <ul
            tabindex="0"
            class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow">
          <li>
            <RouterLink to="/">Home</RouterLink>
          </li>
          <li>
            <RouterLink to="/other">Other</RouterLink>
          </li>
          <li>
            <RouterLink to="/roman">Roman</RouterLink>
          </li>
          <li>
            <RouterLink to="/konrad">Konrad</RouterLink>
          </li>
          <li>
            <RouterLink to="/gabi">Gabi</RouterLink>
          </li>
          <li>
            <RouterLink to="/alicia">Alicia</RouterLink>
          </li>
          <li>
            <a href="http://localhost:8000/register/">Register</a>
          </li>
          <li>
            <a href="http://localhost:8000/register/">Log in</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <RouterView/>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import {RouterView} from "vue-router";

export default defineComponent({
  components: {RouterView},
});

</script>

<style scoped>
</style>
