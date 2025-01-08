<script lang="ts">
import { defineComponent } from 'vue'
import { logout, addUserHobby, deleteUserHobby, fetchAllHobbies } from "../api";
import { useUserStore } from "../store/user";
import { Trash } from "lucide-vue-next";
import { Hobby } from "../api";

export default defineComponent({
  components: { Trash },
  name: "Sidebar",
  setup() {
    const userStore = useUserStore();
    return { userStore };
  },
  data() {
    return {
      hobbies: [] as Hobby[],
      selectedHobby: null as number | null,
      typedHobby: ""
    };
  },
  async mounted() {
    const { hobbies } = await this.fetchAllHobbies();
    this.hobbies = hobbies;
  },
  methods: {
    logout,
    addUserHobby,
    deleteUserHobby,
    fetchAllHobbies,
    showModal() {
      this.selectedHobby = null;
      this.typedHobby = "";
      document.getElementById('add_hobby')?.showModal();
    },
    closeModal() {
      this.selectedHobby = null;
      this.typedHobby = "";
    },
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
        <ul class="flex flex-col gap-1 mb-4">
          <button @click="deleteUserHobby(hobby.id)" v-for="hobby in userStore.getHobbies" :key="hobby.id"
                  class="capitalize text-md font-medium btn bg-slate-700 border-0 hover:bg-slate-500 text-white justify-between">
            {{ hobby.name }}
            <Trash :size="16"/>
          </button>
        </ul>
        <button @click="showModal"
                class="btn w-full mt-auto mb-4 bg-slate-500 border-0 text-white hover:bg-slate-400">Add Hobby
        </button>

        <dialog id="add_hobby" class="modal text-neutral-700" @close="closeModal">
          <div class="modal-box min-w-[50vw]">
            <form method="dialog">
              <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

              <div class="flex w-full my-6">
                <div class="card rounded-box flex-grow place-items-center min-h-20 w-1/2 gap-6 mx-10">
                  <h1>Select an Existing Hobby</h1>
                  <select class="select select-bordered w-full max-w-xs" v-model="selectedHobby">
                    <option selected disabled>Select a Hobby</option>
                    <option v-for="hobby in hobbies" :key="hobby.id" :value="hobby.id">{{ hobby.name }}</option>
                  </select>
                  <button :class="['btn w-full', !selectedHobby && 'btn-disabled']" @click="addUserHobby(hobbies.filter(h => h.id === selectedHobby)[0]?.name)">
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
