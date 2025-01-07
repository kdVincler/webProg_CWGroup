<script lang="ts">
import {defineComponent} from 'vue'
import {useUserStore} from "../store/user";

export default defineComponent({
  name: "EditProfileModal",
  setup() {
    const userStore = useUserStore();
    return {userStore};
  }
})
</script>

<template>
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