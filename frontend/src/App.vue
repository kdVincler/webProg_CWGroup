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
            <a href="http://127.0.0.1:8000/admin/" >Admin Site</a>
          </li>
          <li>
            <a href="http://localhost:8000/register/">Register</a>
          </li>
          <li>
            <a href="http://localhost:8000/login/">Log in</a>
          </li>
          <li>
            <a @click="logout">Log out</a>
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
  methods: {
    async logout(): Promise<void>  {
      try {
        const response = await fetch('http://localhost:8000/logout/', {
          method: 'GET',
          credentials: 'include',
        })

        if (!response.ok) {
          alert("Logout unsuccessful, try again")
        }
      } catch (error: any) {
        alert("Error: " + error)
      }
    }
  }
});

</script>

<style scoped>
</style>
