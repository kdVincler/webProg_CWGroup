<script lang="ts">
import { defineComponent, ref } from "vue";
import { useUserStore } from "../store/user";
import { usePageStore } from "../store/page.ts";
import { logout } from "../api";
import { SlidersHorizontal } from "lucide-vue-next";
import { getInitialBGColour } from "../utils.ts";

export default defineComponent({
  components: { SlidersHorizontal },
  name: "Navbar",
  setup() {
    const userStore = useUserStore();
    const pageStore = usePageStore();

    const filterEnabled = ref(pageStore.isFilterEnabled);
    const filterLow = ref(pageStore.getFilter?.low || 0);
    const filterHigh = ref(pageStore.getFilter?.high || 100);

    const applyFilter = () => {
      if (filterEnabled.value) {
        pageStore.setFilter({ low: filterLow.value, high: filterHigh.value });
      } else {
        pageStore.clearFilter();
      }
    };

    return {
      userStore,
      pageStore,
      filterEnabled,
      filterLow,
      filterHigh,
      applyFilter,
      logout,
      getInitialBGColour,
    };
  },
});
</script>

<template>
  <div class="navbar">
    <div class="flex-1">
      <div class="dropdown">
        <div v-if="$route.path === '/'" tabindex="0" role="button" class="btn btn-ghost text-lg gap-4">
          Filters
          <SlidersHorizontal :size="20" />
        </div>
        <div tabindex="0" class="w-[96vw] md:w-[32rem] dropdown-content menu bg-base-100 rounded-box z-[1] p-2 shadow">
          <div class="flex flex-row items-center justify-between w-full p-4">
            <label class="label cursor-pointer flex flex-row items-center gap-2">
              <input
                type="checkbox"
                class="checkbox"
                v-model="filterEnabled"
              />
              <span class="label-text">Filter by age?</span>
            </label>
            <div class="flex flex-row gap-4 items-center">
              From:
              <input
                type="number"
                placeholder="0"
                class="input input-bordered w-full max-w-[4rem]"
                v-model.number="filterLow"
                :disabled="!filterEnabled"
              />
              To:
              <input
                type="number"
                placeholder="100"
                class="input input-bordered w-full max-w-[4rem]"
                v-model.number="filterHigh"
                :disabled="!filterEnabled"
              />
            </div>
          </div>
          <button class="btn w-full mt-2" @click="applyFilter">Apply</button>
        </div>
      </div>
    </div>
    <div class="flex-none gap-2">
      <div class="dropdown dropdown-end">
        <div tabindex="0" role="button" class="btn btn-ghost btn-circle avatar">
          <div :class="['w-10', 'rounded-full', getInitialBGColour(userStore?.getInitials || '')]">
            <div class="flex flex-row items-center justify-center h-full w-full">
              <span class="w-full text-center uppercase">{{ userStore.getInitials }}</span>
            </div>
          </div>
        </div>
        <ul
          tabindex="0"
          class="menu menu-sm dropdown-content bg-base-100 rounded-box z-[1] mt-3 w-52 p-2 shadow"
        >
          <li>
            <RouterLink to="/">Home</RouterLink>
          </li>
          <li>
            <RouterLink to="/profile">My Profile</RouterLink>
          </li>
          <li>
            <!--TODO: Delete this-->
            <a href="http://127.0.0.1:8000/admin/" target="_blank">Admin Site</a>
          </li>
          <li>
            <a @click="logout">Log out</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
