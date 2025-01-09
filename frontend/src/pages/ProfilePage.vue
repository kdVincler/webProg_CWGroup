<script lang="ts">
import {defineComponent} from "vue";
import {useUserStore} from "../store/user";
import {Mail, Calendar} from "lucide-vue-next";

export default defineComponent({
  components: { Mail, Calendar},
  name: "ProfilePage",
  setup() {
    const userStore = useUserStore();
    return {userStore};
  },
  methods: {
     openModal() {
        (document.getElementById('profile_modal') as HTMLDialogElement).showModal();
      },
      closeModal() {
        (document.getElementById('profile_modal') as HTMLDialogElement).close();
      }
  }
})
</script>

<template>
  <div class="p-6 h-full flex flex-col items-center gap-16 overflow-y-auto">
    <h1 class="text-3xl font-semibold">My Profile</h1>
    <div class="card bg-base-100 min-w-96 shadow-xl ">
      <div class="card-body flex flex-col items-center ">
        <div class="rounded-full h-36 w-36 bg-red-400">
          <div class="flex flex-row items-center justify-center h-full w-full">
            <span class="w-full text-center text-5xl font-semibold text-neutral-700">{{ userStore.getInitials }}</span>
          </div>
        </div>

        <div class="divider font-semibold text-neutral-400">{{ userStore.getName }}</div>
        <h2 class="text-md font-semibold text-neutral-400 self-start flex flex-row gap-2">
          <Mail/>
          {{ userStore.getEmail }}
        </h2>
        <h2 class="text-md font-semibold text-neutral-400 self-start flex flex-row gap-2">
          <Calendar/>
          {{ userStore.getDoB }}
        </h2>

        <div class="divider font-semibold text-neutral-400">Hobbies</div>
        <ul class="flex flex-col w-full px-6 gap-2 list-disc">
          <li class="text-md font-semibold text-neutral-400 self-start text-start" v-for="hobby in userStore.getHobbies" >{{ hobby.name}}</li>
        </ul>

        <div class="card-actions justify-end w-full pt-6">
          <button @click="openModal" class="btn w-full">Edit Profile</button>
        </div>
      </div>
    </div>
  </div>
<!--  <EditProfileModal />-->
  <dialog id="profile_modal" class="modal flex flex-row">
    <div class="w-1/6"/>
    <div class="flex-grow flex items-center justify-center">
      <div class="modal-box">
        <h3 class="text-lg font-semibold">Hello, {{userStore.getName.split(' ')[0]}}.</h3>
        <p class="py-4">Click the button below to close</p>
        <div class="modal-action">
          <form method="dialog">
            <button class="btn">Close</button>
          </form>
        </div>
      </div>
    </div>
  </dialog>
</template>