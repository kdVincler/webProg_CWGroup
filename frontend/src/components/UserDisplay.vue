<script lang="ts">
import {defineComponent} from 'vue'
import {Trophy} from 'lucide-vue-next'
import {sendFriendRequest, rejectFriendRequestOrRemoveFriend} from '../api'
import {PropType} from 'vue'
import {getInitialBGColour} from '../utils'
import {PaginatedUser} from '../store/page'
import { useUserStore } from '../store/user'

export default defineComponent({
  components: {Trophy},
  name: "UserDisplay",
  props: {
    user: {
      type: Object as PropType<PaginatedUser>,
      required: true
    },
    position: {
      type: Number,
      required: true
    },
    isFriend: {
      type: Boolean,
      default: false
    },
    isRequested: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      isFriendData: this.isFriend,
      isRequestedData: this.isRequested
    }
  },
  methods: {
    async addFriend() {
      await sendFriendRequest(this.user.id)
      await useUserStore().updateFriendRequests()
      this.isRequestedData = useUserStore()?.getOutgoingFriendRequests?.some(entry => entry.user2.id === this.user.id) || false
      this.isFriendData = useUserStore()?.getUserFriends?.some(entry => entry.id === this.user.id) || false
      if (this.isFriendData) {
        this.isRequestedData = false
      }

    },
    async removeFriend() {
      this.isFriendData = false
      this.isRequestedData = false
      rejectFriendRequestOrRemoveFriend(this.user.id)
      await useUserStore().updateFriendRequests()

    },
    getInitialBGColour
  }
})
</script>

<template>
  <div class="w-full flex flex-row items-center justify-between my-4 bg-base-100 card shadow-lg p-6">
    <div class="flex-row items-center justify-start flex w-full h-full gap-6">
      <div
          :class="['w-16 h-16 rounded-full', getInitialBGColour(user.name.split(' ').map((n) => n[0]).join('') || '')]">
        <div class="flex flex-row items-center justify-center h-full w-full">
          <span class="w-full text-center text-xl uppercase">{{ user.name.split(' ').map((n) => n[0]).join('') }}</span>
        </div>
      </div>
      <div>
        <h2 class="text-lg font-semibold">{{ user.name }}</h2>
        <h3 class="text-sm text-neutral-500 font-normal"><span class="font-bold">{{ user.similar_hobbies_count }}</span>
          Similar
          Hobbies</h3>
      </div>
    </div>

    <button v-if="isRequestedData" class="btn justify-self-end btn-disabled min-w-32">
      Requested
    </button>
    <button v-else-if="isFriendData" @click="removeFriend" class="btn justify-self-end min-w-32">
      Remove Friend
    </button>
    <button v-else @click="addFriend" class="btn justify-self-end min-w-32">
      Add Friend
    </button>
  </div>


</template>