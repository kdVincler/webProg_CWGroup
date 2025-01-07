<script lang="ts">
import {defineComponent} from "vue";
import {useUserStore} from "../store/user";
import {Mail, Calendar} from "lucide-vue-next";
import EditProfileModal from "@/components/EditProfileModal.vue";

export default defineComponent({
  components: {EditProfileModal, Mail, Calendar},
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
  <div class="p-6 h-full flex flex-col items-center gap-16">
    <h1 class="text-3xl font-semibold">My Profile</h1>
    <div class="card bg-base-100 w-96 shadow-xl">
      <div class="card-body flex flex-col items-center">
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
          <li class="text-md font-semibold text-neutral-400 self-start text-start">Snowboarding</li>
          <li class="text-md font-semibold text-neutral-400 self-start text-start">Hiking</li>
          <li class="text-md font-semibold text-neutral-400 self-start text-start">Biking</li>
        </ul>

        <div class="card-actions justify-end w-full pt-6">
          <button @click="openModal" class="btn w-full">Edit Profile</button>
        </div>
      </div>
    </div>
  </div>
  <EditProfileModal />
</template>