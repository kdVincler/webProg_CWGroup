<script lang="ts">
import {defineComponent} from 'vue';
import {Trophy, CircleHelp} from 'lucide-vue-next';
import {PropType} from 'vue';
import {sendFriendRequest, rejectFriendRequestOrRemoveFriend} from "../api.ts";
import {PaginatedUser} from '../store/page.ts';
import {useUserStore} from '../store/user.ts';
import UserDisplay from "./UserDisplay.vue";

export default defineComponent({
  components: {UserDisplay, Trophy, CircleHelp},
  name: "PodiumDisplay",
  props: {
    users: {
      type: Array as PropType<PaginatedUser[]>,
      required: true,
    },
    isFriend: {
      type: Array as PropType<boolean[]>,
      default: [false, false, false],
    },
    isRequested: {
      type: Array as PropType<boolean[]>,
      default: [false, false, false],
    },
  },
  methods: {
    async addFriend(index: number) {
      await sendFriendRequest(this.users[index].id)
      await useUserStore().updateFriendRequests()
    },
    async removeFriend(index: number) {
      await rejectFriendRequestOrRemoveFriend(this.users[index].id)
      await useUserStore().updateFriendRequests()
    },
  },
});
</script>

<template>
  <h1 class="text-3xl font-semibold text-center hidden lg:block">Top 3 Users Like You</h1>
  <div class="block lg:hidden">
    <UserDisplay v-if="users.length > 0" :user="users[0]" :isFriend="isFriend[0]"
                 :isRequested="isRequested[0]" :position="1"/>
    <UserDisplay v-if="users.length > 1" :user="users[1]" :isFriend="isFriend[1]"
                 :isRequested="isRequested[1]" :position="2"/>
    <UserDisplay v-if="users.length > 2" :user="users[2]" :isFriend="isFriend[2]"
                 :isRequested="isRequested[2]" :position="3"/>
  </div>
  <div class="w-full  hidden lg:flex flex-row justify-center items-end my-10" id="podium_third">
    <div class="shadow-lg p-6 h-[50vh] w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between">
      <div class="flex flex-col items-center">
        <div class="rounded-full lg:h-36 lg:w-36 w-20 h-20 bg-orange-500 flex items-center justify-center dark:text-base-100">
          <Trophy :size="64"/>
        </div>
        <h2 class="lg:text-2xl font-semibold text-center mt-2">{{ users[2]?.name }}</h2>
        <div
            class="tooltip tooltip-bottom w-full"
            :data-tip="
          users[2]?.similar_hobbies_count === 0
          ? `You don't share any hobbies`
          : `You share the following hobbies: ${users[2]?.similar_hobbies.map(hobby => hobby.name).join(', ')}`"
        >
          <h3 class="mt-4 cursor-pointer lg:text-sm text-xs  text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            {{ users[2]?.similar_hobbies_count || 0 }} Similar Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button v-if="isRequested[2]" class="btn justify-self-end btn-disabled w-full">
        Requested
      </button>
      <button v-else-if="isFriend[2]" @click="removeFriend(2)" class="btn justify-self-end w-full">
        Remove Friend
      </button>
      <button v-else @click="addFriend(2)" class="btn justify-self-end w-full" :id="'button'+3">
        Add Friend
      </button>
    </div>


    <!-- First Place -->
    <div class="shadow-lg p-6 h-[70vh] w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between" id="podium_first">
      <div class="flex flex-col items-center">
        <div class="rounded-full lg:h-36 lg:w-36 w-20 h-20  bg-yellow-400 flex items-center justify-center dark:text-base-100">
          <Trophy :size="64"/>
        </div>
        <h2 class="lg:text-2xl font-semibold text-center mt-2">{{ users[0]?.name }}</h2>
        <div
            class="tooltip tooltip-bottom w-full"
            :data-tip="
          users[0]?.similar_hobbies_count === 0
          ? `You don't share any hobbies`
          : `You share the following hobbies: ${users[0]?.similar_hobbies.map(hobby => hobby.name).join(', ')}`"
        >
          <h3 class="mt-4 cursor-pointer lg:text-sm text-xs text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            {{ users[0]?.similar_hobbies_count || 0 }} Similar Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button v-if="isRequested[0]" class="btn justify-self-end btn-disabled w-full">
        Requested
      </button>
      <button v-else-if="isFriend[0]" @click="removeFriend(0)" class="btn justify-self-end w-full">
        Remove Friend
      </button>
      <button v-else @click="addFriend(0)" class="btn justify-self-end w-full" :id="'button'+1">
        Add Friend
      </button>
    </div>

    <!-- Second Place -->
    <div class="shadow-lg p-6 h-[60vh] w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between" id="podium_second">
      <div class="flex flex-col items-center">
        <div class="rounded-full lg:h-36 lg:w-36 w-20 h-20  bg-gray-300 flex items-center justify-center dark:text-base-100">
          <Trophy :size="64"/>
        </div>
        <h2 class="lg:text-2xl font-semibold text-center mt-2">{{ users[1]?.name }}</h2>
        <div
            class="tooltip tooltip-bottom w-full"
            :data-tip="
          users[1]?.similar_hobbies_count === 0
          ? `You don't share any hobbies`
          : `You share the following hobbies: ${users[1]?.similar_hobbies.map(hobby => hobby.name).join(', ')}`"
        >
          <h3 class="mt-4 cursor-pointer lg:text-sm text-xs  text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            {{ users[1]?.similar_hobbies_count || 0 }} Similar Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button v-if="isRequested[1]" class="btn justify-self-end btn-disabled w-full">
        Requested
      </button>
      <button v-else-if="isFriend[1]" @click="removeFriend(1)" class="btn justify-self-end w-full">
        Remove Friend
      </button>
      <button v-else @click="addFriend(1)" class="btn justify-self-end w-full" :id="'button'+2">
        Add Friend
      </button>
    </div>
  </div>
</template>
