<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import UserDisplay from "../components/UserDisplay.vue";
import PodiumDisplay from "../components/PodiumDisplay.vue";
import { getUsersPaginated } from "../api";

export default defineComponent({
  components: { PodiumDisplay, UserDisplay },
  name: "MainPage",
  setup() {
    const similar_users = ref<any[]>([]); // Declare `similar_users` as a ref
    const loading = ref(true); // Track loading state

    onMounted(async () => {
      try {
        const paginatedData = await getUsersPaginated(0); // Wait for the data to load
        similar_users.value = paginatedData?.page?.users || []; // Safely handle potential undefined values
      } catch (error) {
        console.error("Error loading users:", error);
      } finally {
        loading.value = false; // Data loading is complete
      }
    });

    return {
      similar_users,
      loading,
    };
  },
});
</script>

<template>
  <div v-if="similar_users.length > 2" class="h-full overflow-y-auto px-6">
    <PodiumDisplay v-if="!loading" :first_user="similar_users[0]" :second_user="similar_users[1]" :third_user="similar_users[2]" />
    <div v-if="loading" class="text-center">Loading users...</div>
    <div v-else>
      <UserDisplay
        v-for="(user, index) in similar_users.slice(3)"
        :key="index"
        :position="index + 4"
        :user="user"
      />
    </div>
  </div>
  <div v-else class="h-full overflow-y-auto px-6">
    <div v-if="loading" class="text-center">Loading users...</div>
    <div v-else>
      <UserDisplay
        v-for="(user, index) in similar_users"
        :key="index"
        :position="index + 1"
        :user="user"
      />
    </div>
  </div>
  <div class="join w-full flex justify-center mb-6 mt-2">
    <button class="join-item btn bg-base-100">1</button>
    <button class="join-item btn bg-base-100">2</button>
    <button class="join-item btn btn-disabled">...</button>
    <button class="join-item btn bg-base-100">4</button>
    <button class="join-item btn bg-base-100">5</button>
  </div>
</template>
