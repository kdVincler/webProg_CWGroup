<script lang="ts">
import {defineComponent} from 'vue'
import {useUserStore} from "../store/user";
import {logout} from "../api";
import {SlidersHorizontal} from "lucide-vue-next";

export default defineComponent({
  components: {SlidersHorizontal},
  name: "Navbar",
  data() {
    return {
      userStore: useUserStore(),
    }
  },
  methods: {
    logout,
    generateBgColor(initials: string) {
      const colors = [
        'bg-red-500',
        'bg-blue-500',
        'bg-green-500',
        'bg-yellow-500',
        'bg-indigo-500',
        'bg-orange-500',
        'bg-pink-500',
      ]
      try {
        if (initials.length === 0) {
          return colors[0]
        }
      } catch (e) {
        return colors[0]
      }
      const charCode = initials.charCodeAt(0)
      return colors[charCode % colors.length]
    }
  }
})
</script>

<template>
  <div class="navbar">
    <div class="flex-1">
            <RouterLink to="/" class="btn btn-ghost text-lg gap-4">Filters <SlidersHorizontal size="20" /></RouterLink>
    </div>
    <div class="flex-none gap-2">
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div :class="['w-10', 'rounded-full', generateBgColor(userStore.getInitials)]">
            <div class="flex flex-row items-center justify-center h-full w-full">
              <span class="w-full text-center">{{ userStore.getInitials }}</span>
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
            <RouterLink to="/profile">Profile</RouterLink>
          </li>
          <li>
            <a href="http://127.0.0.1:8000/admin/">Admin Site</a>
          </li>
          <li>
            <a @click="logout">Log out</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>