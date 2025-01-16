<script lang="ts">
import {defineComponent, onMounted} from 'vue'
import {
  logout,
  addUserHobby,
  deleteUserHobby,
  fetchAllHobbies,
  acceptFriendRequest,
  rejectFriendRequestOrRemoveFriend,
} from "../api";
import {User, FriendRequestUser, useUserStore} from "../store/user";
import {useHobbiesStore, Hobby} from '../store/hobbies';
import {Trash, Check, X, Mail} from "lucide-vue-next";

export default defineComponent({
  components: {Trash, Check, X, Mail},
  name: "Sidebar",
  setup() {
    const userStore = useUserStore();
    const hobbiesStore = useHobbiesStore();

    onMounted(async () => {
      if (userStore.getIncomingFriendRequests === undefined || userStore.getUserFriends === undefined) {
        await userStore.updateFriendRequests()
      }
      if (hobbiesStore.getAllHobbies == undefined) {
        await hobbiesStore.populate()
      }
    });
    return {userStore, hobbiesStore};
  },
  computed: {
    friendRequests(): FriendRequestUser[] | [] {
      return this.userStore.getIncomingFriendRequests || []
    },
    friends(): User[] | [] {
      return this.userStore.getUserFriends || []

    },
    hobbies(): Hobby[] | [] {
      return this.hobbiesStore.getAllHobbies || []
    }
  },
  data() {
    return {
      selectedHobby: null as number | null,
      typedHobby: "",
    };
  },
  methods: {
    logout,
    addUserHobby,
    deleteUserHobby,
    fetchAllHobbies,
    showModal() {
      this.selectedHobby = null;
      this.typedHobby = "";
      const dialog = document.getElementById('add_hobby') as HTMLDialogElement;
      dialog?.showModal();
    },
    closeModal() {
      this.selectedHobby = null;
      this.typedHobby = "";
    },
    acceptRequest(id: number) {
      acceptFriendRequest(id)
    },
    rejectRequest(id: number) {
      rejectFriendRequestOrRemoveFriend(id)
    }
  }
})
</script>

<template>
  <div
      class="h-screen bg-slate-600 dark:bg-base-300 w-1/5 px-6 py-2 text-base-200 dark:text-base-content hidden md:flex flex-col items-start">
    <RouterLink to="/" class="btn btn-ghost text-xl italic">Hobby 24</RouterLink>

    <div class="collapse collapse-arrow bg-none my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">My Hobbies</div>
      <div class="collapse-content">
        <ul class="flex flex-col gap-1 mb-4">
          <button @click="deleteUserHobby(hobby.id)" v-for="hobby in userStore.getHobbies" :key="hobby.id"
                  class="capitalize text-md font-medium btn bg-slate-700 dark:bg-base-200 border-0 hover:bg-slate-500 dark:hover:bg-base-100 text-white justify-between">
            {{ hobby.name }}
            <Trash :size="16"/>
          </button>
        </ul>
        <button @click="showModal"
                class="btn w-full mt-auto mb-4 bg-slate-500 dark:bg-base-300 border-0 text-white hover:bg-slate-400 dark:hover:bg-base-100">
          Add Hobby
        </button>

        <dialog id="add_hobby" class="modal text-neutral-700" @close="closeModal">
          <div class="modal-box min-w-[50vw]">
            <form method="dialog">
              <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

              <div class="flex w-full my-6 dark:text-base-content">
                <div class="card rounded-box flex-grow place-items-center min-h-20 w-1/2 gap-6 mx-10">
                  <h1>Select an Existing Hobby</h1>
                  <select class="select select-bordered w-full max-w-xs" v-model="selectedHobby">
                    <option selected disabled>Select a Hobby</option>
                    <option v-for="hobby in hobbies" :key="hobby.id" :value="hobby.id">{{ hobby.name }}</option>
                  </select>
                  <button :class="['btn w-full', !selectedHobby && 'btn-disabled']"
                          @click="addUserHobby(hobbies.filter(h => h.id === selectedHobby)[0]?.name)">
                    Add Hobby
                  </button>
                </div>

                <div class="divider divider-horizontal">OR</div>

                <div class="card rounded-box flex-grow place-items-center min-h-20 w-1/2 gap-6 mx-10">
                  <h1>Add a New Hobby</h1>
                  <input type="text" placeholder="Type here..." class="input input-bordered w-full max-w-xs"
                         v-model="typedHobby"/>
                  <button :class="['btn w-full', !typedHobby && 'btn-disabled']" @click="addUserHobby(typedHobby);">
                    Add Hobby
                  </button>
                </div>
              </div>
            </form>
          </div>
        </dialog>
      </div>
    </div>

    <div class="collapse collapse-arrow bg-none  my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">Friends <span v-if="friends.length>0">
        ({{ friends.length }})
      </span></div>
      <div class="collapse-content">
        <ul class="flex flex-col gap-1 mb-4">
          <a :href="'mailto:' + friend.email" v-for="friend in friends" :key="friend.id"
             class="capitalize text-md font-medium btn bg-slate-700 dark:bg-base-200 border-0 hover:bg-slate-500 dark:hover:bg-base-100 text-white justify-between">
            {{ friend.name }}
            <Mail :size="16"/>
          </a>
        </ul>
      </div>
    </div>
    <div class="collapse collapse-arrow bg-none  my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">Friend Requests <span v-if="friendRequests.length>0">
        ({{ friendRequests.length }})
      </span>
      </div>
      <div class="collapse-content">
        <ul class="flex flex-col gap-1 mb-4">
          <div v-for="request in friendRequests" :key="request.user1.id"
               class="capitalize text-md font-medium  bg-slate-700 dark:bg-base-200 rounded-lg flex flex-row p-2 px-4 text-white justify-between items-center">
            {{ request.user1.name }}
            <div class="flex flex-row-reverse items-center gap-1">
              <button @click="acceptRequest(request.user1.id)"
                      class="btn bg-slate-500 hover:bg-slate-400 dark:bg-base-100 dark:hover:bg-slate-700 border-0 h-8 min-h-0 aspect-square p-0">
                <Check :size="16" color="white"/>
              </button>
              <button @click="rejectRequest(request.user1.id)"
                      class="btn bg-slate-500 dark:bg-base-100 dark:hover:bg-red-800 hover:bg-slate-400 border-0 h-8 min-h-0 aspect-square p-0 ">
                <X :size="16" color="white"/>
              </button>
            </div>

          </div>
        </ul>
      </div>
    </div>

    <button id="sidebar-logout" @click="logout"
            class="btn w-full mt-auto mb-4 bg-slate-500 border-0 text-white hover:bg-slate-400 dark:bg-base-200 dark:hover:bg-base-100">
      Logout
    </button>
  </div>
</template>
