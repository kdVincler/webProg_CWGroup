<script lang="ts">
import {defineComponent, ref, onMounted} from "vue";
import UserDisplay from "../components/UserDisplay.vue";
import PodiumDisplay from "../components/PodiumDisplay.vue";
import {getFriendRequests, getFriends} from "../api";
import {usePageStore, PaginatedUser} from "../store/page";

export default defineComponent({
  components: {PodiumDisplay, UserDisplay},
  name: "MainPage",
  setup() {
    const loading = ref(true);
    const page = ref(1);

    const outgoingRequests = ref([]);
    const friends = ref([]);

    const pageStore = usePageStore();

    onMounted(async () => {
      try {
        if (pageStore.getPage === undefined) {
          await pageStore.paginate(page.value)
        }

        const fr = await getFriendRequests();
        outgoingRequests.value = fr.outgoing_requests;

        const f = await getFriends();
        friends.value = f.friends;
      } catch (error) {
        console.error("Error loading users:", error);
      } finally {
        loading.value = false; // Data loading is complete
      }
    });

    return {
      loading,
      page,
      outgoingRequests,
      friends,
      pageStore
    };
  },
  methods: {
    async changePage(page: number) {
      this.page = page;
      this.loading = true;
      try {
        await this.pageStore.paginate(this.page)
      } catch (error) {
        console.error("Error loading users:", error);
      } finally {
        this.loading = false; // Data loading is complete
      }
    }
  },
  computed: {
    similar_users(): PaginatedUser[] | [] {
      return this.pageStore.getUsers || []
    },
    pages(): number {
      return this.pageStore.getTotalPages || 1
    }
  }
});
</script>

<template>
  <div v-if="similar_users.length > 2 && page == 1" class="h-full overflow-y-auto px-6">
    <PodiumDisplay v-if="!loading" :users="[similar_users[0], similar_users[1], similar_users[2]]"
                   :is-friend="[friends.some(f => f.id === similar_users[0].id),
    friends.some(f => f.id === similar_users[1].id),friends.some(f => f.id === similar_users[2].id)]"
                   :is-requested="[outgoingRequests.some(r => r.user2.id === similar_users[0].id),
    outgoingRequests.some(r => r.user2.id === similar_users[1].id),outgoingRequests.some(r => r.user2.id === similar_users[2].id)]"

    />
    <div v-if="loading" class="text-center">Loading users...</div>
    <div v-else>
      <UserDisplay
          v-for="(user, index) in similar_users.slice(3)"
          :key="index"
          :position="index + 4"
          :user="user"
          :is-friend="friends.some(f => f.id === user.id)"
          :is-requested="outgoingRequests.some(r => r.user2.id === user.id)"
      />
    </div>
  </div>
  <div v-else class="h-full overflow-y-auto px-6">
    <div v-if="loading" class="text-center">Loading users...</div>
    <div v-else>
      <UserDisplay
          v-for="(user, index) in similar_users"
          :key="index"
          :position="index + 1 + ((page-1) * 10)"
          :user="user"
          :is-friend="friends.some(f => f.id === user.id)"
          :is-requested="outgoingRequests.some(r => r.user2.id === user.id)"
      />
    </div>
  </div>
  <div class="join w-full flex justify-center mb-6 mt-2">
    <button class="join-item btn bg-base-100" :class="page == i && 'btn-disabled'" v-for="i in pages"
            @click="changePage(i)">{{ i }}
    </button>
  </div>
</template>
