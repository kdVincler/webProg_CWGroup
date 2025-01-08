<script lang="ts">
import {defineComponent} from 'vue'
import {logout, addUserHobby, deleteUserHobby} from "../api";
import {useUserStore} from "../store/user";
import {Trash} from "lucide-vue-next";

export default defineComponent({
  components: {Trash},
  name: "Sidebar",
  setup() {
    const userStore = useUserStore();
    return {userStore};
  },
  methods: {
    logout,
    addUserHobby,
    deleteUserHobby,
    showModal() {
      document.getElementById('add_hobby')?.showModal();
    }
  }
})
</script>

<template>
  <div class="h-screen bg-slate-600 w-1/6 px-6 py-2 text-base-200 flex flex-col items-start">
    <RouterLink to="/" class="btn btn-ghost text-xl italic">Hobby 24</RouterLink>
    <div class="collapse collapse-arrow bg-slate-600 my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">My Hobbies</div>
      <div class="collapse-content">
        <ul class="flex flex-col gap-1 mb-4 ">
          <button @click="deleteUserHobby(hobby.id)" v-for="hobby in userStore.getHobbies" :key="hobby.id"
                  class="capitalize text-md font-medium btn bg-slate-700 border-0 hover:bg-slate-500 text-white justify-between">
            {{ hobby.name }}{{ hobby.id }}
            <Trash size="16"/>
          </button>
        </ul>
        <button @click="showModal"
                class="btn w-full mt-auto mb-4 bg-slate-500 border-0 text-white hover:bg-slate-400">Add Hobby
        </button>
        <dialog id="add_hobby" className="modal text-neutral-700">
          <div className="modal-box">
            <form method="dialog">
              <button className="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>
            </form>
            <div class="flex w-full mt-6">
              <div class="card rounded-box flex-grow place-items-center min-h-20 w-1/2">
                <h1>Select an Existing Hobby</h1>
              </div>
              <div class="divider divider-horizontal">OR</div>
              <div class="card rounded-box flex-grow place-items-center min-h-20 w-1/2">
                <h1>Add a New Hobby</h1>
              </div>
            </div>
          </div>
        </dialog>
      </div>
    </div>
    <div class="collapse collapse-arrow bg-slate-600 my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">Friends</div>
      <div class="collapse-content">
        <p>List of friends!</p>
      </div>
    </div>
    <div class="collapse collapse-arrow bg-slate-600 my-2">
      <input type="radio" name="my-accordion-2"/>
      <div class="collapse-title text-md font-medium">Friend Requests (1)</div>
      <div class="collapse-content">
        <p>List of friend requests goes here!</p>
      </div>
    </div>
    <button @click="logout" class="btn w-full mt-auto mb-4 bg-slate-500 border-0 text-white hover:bg-slate-400">Logout
    </button>
  </div>

</template>