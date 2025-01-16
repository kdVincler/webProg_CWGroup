<script lang="ts">
import {defineComponent, ref, onMounted} from "vue";
import UserDisplay from "../components/UserDisplay.vue";
import PodiumDisplay from "../components/PodiumDisplay.vue";
import {usePageStore, PaginatedUser} from "../store/page";
import {User, FriendRequestUser, useUserStore} from "../store/user";

export default defineComponent({
  components: {PodiumDisplay, UserDisplay},
  name: "MainPage",
  setup() {
    const loading = ref(true);
    const page = ref(1);

    const pageStore = usePageStore();
    const userStore = useUserStore();

    onMounted(async () => {
      try {
        if (pageStore.getPage === undefined) {
          await pageStore.paginate(page.value)
        }
        if (userStore.getOutgoingFriendRequests === undefined || userStore.getUserFriends === undefined) {
          await userStore.updateFriendRequests()
        }
      } catch (error) {
        console.error("Error loading users:", error);
      } finally {
        loading.value = false;
      }
    });

    return {
      loading,
      page,
      pageStore,
      userStore
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
        this.loading = false;
      }
    }
  },
  computed: {
    similar_users(): PaginatedUser[] | [] {
      return this.pageStore.getUsers || []
    },
    pages(): number {
      return this.pageStore.getTotalPages || 1
    },
    outgoingRequests(): FriendRequestUser[] | [] {
      return this.userStore.getOutgoingFriendRequests || []
    },
    friends(): User[] | [] {
      return this.userStore.getUserFriends || []
    },
    isFriend(): (user: PaginatedUser) => boolean {
      // computed property that returns a function with one positional argument, returning a boolean
      // so return types are: computed property *returns* function, function(i) *returns* boolean
      return (user: PaginatedUser): boolean => {
        // friends.some(f => f.id === similar_users[index].id)
        return this.friends.some(f => f.id === user.id)
      }
    },
    isRequested(): (user: PaginatedUser) => boolean {
      // same return type as isFriend property
      return (user: PaginatedUser): boolean => {
        // outgoingRequests.some(r => r.user2.id === similar_users[index].id)
        return this.outgoingRequests.some(r => r.user2.id === user.id)
      }
    }
  }
});
</script>

<template>
  <div v-if="similar_users.length > 2 && page == 1" class="h-full overflow-y-auto px-6">
    <PodiumDisplay v-if="!loading" :users="[similar_users[0], similar_users[1], similar_users[2]]"
                   :is-friend="[isFriend(similar_users[0]), isFriend(similar_users[1]), isFriend(similar_users[2])]"
                   :is-requested="[isRequested(similar_users[0]), isRequested(similar_users[1]), isRequested(similar_users[2])]"

    />
    <div v-if="loading" class="text-center">Loading users...</div>
    <div v-else>
      <UserDisplay
          v-for="(user, index) in similar_users.slice(3)"
          :key="index"
          :position="index + 4"
          :user="user"
          :is-friend="isFriend(user)"
          :is-requested="isRequested(user)"
      />
    </div>
  </div>
  <div v-else class="h-full overflow-y-auto px-6">
    <div v-if="loading" class="text-center">Loading users...</div>
    <div v-else-if="!loading && similar_users.length === 0" class="text-center">No users to display.</div>
    <div v-else>
      <UserDisplay
          v-for="(user, index) in similar_users"
          :key="index"
          :position="index + 1 + ((page-1) * 10)"
          :user="user"
          :is-friend="isFriend(user)"
          :is-requested="isRequested(user)"
      />
    </div>
  </div>
  <div class="join w-full flex justify-center mb-6 mt-2">
    <button class="join-item btn bg-base-100" :class="page == i && 'btn-disabled'" v-for="i in pages"
            @click="changePage(i)">{{ i }}
    </button>
  </div>
</template>
