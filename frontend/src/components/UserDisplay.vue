<script lang="ts">
import {defineComponent} from 'vue'
import {UserMinus, UserPlus, UserCheck, CircleHelp} from 'lucide-vue-next'
import {sendFriendRequest, rejectFriendRequestOrRemoveFriend} from '../api'
import {PropType} from 'vue'
import {getInitialBGColour} from '../utils'
import {PaginatedUser} from '../store/page'
import {useUserStore} from '../store/user'

export default defineComponent({
  components: {UserPlus, UserMinus, UserCheck, CircleHelp},
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
  methods: {
    async addFriend() {
      await sendFriendRequest(this.user.id)
      await useUserStore().updateFriendRequests()
    },
    async removeFriend() {
      rejectFriendRequestOrRemoveFriend(this.user.id)
      await useUserStore().updateFriendRequests()
    },
    getInitialBGColour
  }
})
</script>

<template>
  <div class="w-full flex flex-row items-center justify-between my-4 bg-base-100 card shadow-lg p-6" :id="`user_display_${position}`">
    <div class="flex-row items-center justify-start flex w-full h-full gap-6">
      <div
          :class="['w-16 h-16 rounded-full', getInitialBGColour(user.name.split(' ').map((n) => n[0]).join('') || '')]">
        <div class="flex flex-row items-center justify-center h-full w-full">
          <span class="w-full text-center text-xl uppercase">{{ user.name.split(' ').map((n) => n[0]).join('') }}</span>
        </div>
      </div>
      <div>
        <h2 class="text-lg font-semibold">{{ user.name }}</h2>
        <div
            class="tooltip tooltip-bottom"
            :data-tip="
            user.similar_hobbies_count === 0
            ? `You don't share any hobbies`
            : `You share the following hobbies: ${user.similar_hobbies.map(hobby => hobby.name).join(', ')}`"
        >
          <h3 class="text-sm text-neutral-500 font-normal flex flex-row items-center justify-center gap-1"><span class="font-bold">{{ user.similar_hobbies_count }}</span>
            Similar
            Hobbies
            <CircleHelp :size="16"/>
          </h3>
        </div>
      </div>
    </div>

    <button v-if="isRequested" class="btn justify-self-end btn-disabled sm:min-w-32 w-12">
      <span class="sm:hidden block">
        <UserCheck/>
      </span>
      <span class="sm:block hidden">
      Requested
        </span>
    </button>
    <button v-else-if="isFriend" @click="removeFriend" class="btn justify-self-end sm:min-w-32 w-12">
      <span class="sm:hidden block">
        <UserMinus/>
      </span>
      <span class="sm:block hidden">
      Remove Friend
        </span>
    </button>
    <button v-else @click="addFriend" class="btn justify-self-end sm:min-w-32 w-12" :id="'button'+position">
      <span class="sm:hidden block">
        <UserPlus/>
      </span>
      <span class="sm:block hidden">
      Add Friend
        </span>
    </button>
  </div>


</template>