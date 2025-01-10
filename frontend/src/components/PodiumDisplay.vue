<script lang="ts">
import {defineComponent} from 'vue';
import {Trophy, CircleHelp} from 'lucide-vue-next';
import {PropType} from 'vue';
import {sendFriendRequest, rejectFriendRequestOrRemoveFriend} from "../api.ts";
import {PaginatedUser} from '../store/page.ts';

export default defineComponent({
  components: {Trophy, CircleHelp},
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
  data() {
    return {
      isFriendData: this.isFriend,
      isRequestedData: this.isRequested,
    };
  },
  methods: {
    addFriend(index: number) {
      this.isRequestedData[index] = true;
      sendFriendRequest(this.users[index].id)
    },
    removeFriend(index: number) {
      this.isFriendData[index] = false;
      this.isRequestedData[index] = false;
      rejectFriendRequestOrRemoveFriend(this.users[index].id)
    },
  },
});
</script>

<template>
  <h1 class="text-3xl font-semibold text-center">Top 3 Users Like You</h1>
  <div class="w-full flex flex-row justify-center items-end my-10">

    <div class="shadow-lg p-6 h-[50vh] w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between">
      <div>
        <div class="rounded-full h-36 w-36 bg-orange-500 flex items-center justify-center">
          <Trophy :size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">{{ users[2]?.name }}</h2>
        <div
            class="tooltip tooltip-bottom w-full"
            :data-tip="
          users[2]?.similar_hobbies_count === 0
          ? `You don't share any hobbies`
          : `You share the following hobbies: ${users[2]?.similar_hobbies.map(hobby => hobby.name).join(', ')}`"
        >
          <h3 class="mt-4 cursor-pointer text-sm text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            {{ users[2]?.similar_hobbies_count || 0 }} Similar Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button v-if="isRequestedData[2]" class="btn justify-self-end btn-disabled w-full">
        Requested
      </button>
      <button v-else-if="isFriendData[2]" @click="removeFriend(2)" class="btn justify-self-end w-full">
        Remove Friend
      </button>
      <button v-else @click="addFriend(2)" class="btn justify-self-end w-full">
        Add Friend
      </button>
    </div>


    <!-- First Place -->
    <div class="shadow-lg p-6 h-[70vh] w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between">
      <div>
        <div class="rounded-full h-36 w-36 bg-yellow-400 flex items-center justify-center">
          <Trophy :size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">{{ users[0]?.name }}</h2>
        <div
            class="tooltip tooltip-bottom w-full"
            :data-tip="
          users[0]?.similar_hobbies_count === 0
          ? `You don't share any hobbies`
          : `You share the following hobbies: ${users[0]?.similar_hobbies.map(hobby => hobby.name).join(', ')}`"
        >
          <h3 class="mt-4 cursor-pointer text-sm text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            {{ users[0]?.similar_hobbies_count || 0 }} Similar Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button v-if="isRequestedData[0]" class="btn justify-self-end btn-disabled w-full">
        Requested
      </button>
      <button v-else-if="isFriendData[0]" @click="removeFriend(0)" class="btn justify-self-end w-full">
        Remove Friend
      </button>
      <button v-else @click="addFriend(0)" class="btn justify-self-end w-full">
        Add Friend
      </button>
    </div>

    <!-- Second Place -->
    <div class="shadow-lg p-6 h-[60vh] w-[14vw] bg-base-100 mx-1 flex flex-col items-center justify-between">
      <div>
        <div class="rounded-full h-36 w-36 bg-gray-300 flex items-center justify-center">
          <Trophy :size="64"/>
        </div>
        <h2 class="text-2xl font-semibold text-center mt-2">{{ users[1]?.name }}</h2>
        <div
            class="tooltip tooltip-bottom w-full"
            :data-tip="
          users[1]?.similar_hobbies_count === 0
          ? `You don't share any hobbies`
          : `You share the following hobbies: ${users[1]?.similar_hobbies.map(hobby => hobby.name).join(', ')}`"
        >
          <h3 class="mt-4 cursor-pointer text-sm text-neutral-400 font-semibold text-center w-full flex flex-row items-center justify-center gap-1">
            {{ users[1]?.similar_hobbies_count || 0 }} Similar Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
        <div class="divider"></div>
      </div>
      <button v-if="isRequestedData[1]" class="btn justify-self-end btn-disabled w-full">
        Requested
      </button>
      <button v-else-if="isFriendData[1]" @click="removeFriend(1)" class="btn justify-self-end w-full">
        Remove Friend
      </button>
      <button v-else @click="addFriend(1)" class="btn justify-self-end w-full">
        Add Friend
      </button>
    </div>
  </div>
</template>
