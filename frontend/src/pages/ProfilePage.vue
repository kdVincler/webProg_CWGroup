<script lang="ts">
import {defineComponent, ref, onMounted} from "vue";
import {FriendRequestUser, User, useUserStore} from "../store/user";
import {Mail, Calendar, PencilLine, X, Eye, EyeOff, Trash, Check} from "lucide-vue-next";
import {EditUser, updateUser, deleteUser, addUserHobby, deleteUserHobby, acceptFriendRequest, rejectFriendRequestOrRemoveFriend} from "../api";
import {getInitialBGColour} from "../utils.ts";
import {Hobby, useHobbiesStore} from "../store/hobbies.ts";

export default defineComponent({
  components: {Mail, Calendar, PencilLine, X, Eye, EyeOff, Trash, Check},
  name: "ProfilePage",
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

    function createEditUser(): EditUser {
      return {
        name_changed: false,
        name: userStore.getName || "",
        email_changed: false,
        email: userStore.getEmail || "",
        dob_changed: false,
        dob: userStore.getDoB || "",
        password_changed: false,
        old_password: "",
        new_password: "",
        confirm_new_password: ""
      }
    }

    const editUser = ref<EditUser>(createEditUser())
    const showOldPassword = ref(false)
    const showNewPassword = ref(false)
    const showConfirmNewPassword = ref(false)
    const errorText = ref("")

    return {
      userStore,
      hobbiesStore,
      editUser,
      showOldPassword,
      showNewPassword,
      showConfirmNewPassword,
      errorText
    };
  },
  methods: {
    addUserHobby,
    deleteUserHobby,
    acceptFriendRequest,
    rejectFriendRequestOrRemoveFriend,
    updateUser,
    deleteUser,
    getInitialBGColour,
    openModal(modal: String) {
      if (modal == "add_hobby") {
        this.selectedHobby = null;
        this.typedHobby = "";
      }
      (document.getElementById(`${modal}_profile_modal`) as HTMLDialogElement).showModal();
    },
    closeModal(modal: String) {
      (document.getElementById(`${modal}_profile_modal`) as HTMLDialogElement).close();
      if (modal == "edit") {
        this.editUser = this.resetEditUser()
      }
      if (modal == "error") {
        this.errorText = ""
      }
      if (modal == "add_hobby") {
        this.selectedHobby = null;
        this.typedHobby = "";
      }
    },
    async submitForm() {
      if (this.editUser.password_changed && (this.editUser.old_password == "" || this.editUser.new_password == "" || this.editUser.confirm_new_password == "")) {
        // user submits without filling in one or more of the password fields after selecting the option tho change them
        this.errorText = "Please fill in the Old Password, New Password and Confirm New Password fields to edit your password"
        this.openModal("error")
        return
      } else if (this.editUser.password_changed && (this.editUser.new_password == this.editUser.old_password)) {
        // old password and new password match
        this.errorText = "New Password Can't Be Old Password"
        this.openModal("error")
        return
      } else if (this.editUser.password_changed && (this.editUser.new_password !== this.editUser.confirm_new_password)) {
        // new password and confirm new password don't match
        this.errorText = "New Password And Confirm New Password Don't Match"
        this.openModal("error")
        return
      } else if (this.editUser.name_changed || this.editUser.email_changed || this.editUser.dob_changed || this.editUser.password_changed) {
        // user submits the form indicating change with password fields validated or not changed
        try {
          await updateUser(this.editUser)
          this.editUser = this.resetEditUser()
        } catch (error: any) {
          this.errorText = error
          this.openModal("error")
          return
        }
        this.closeModal("edit")
      }
    },
    async onDelete() {
      try {
        await deleteUser()
      } catch (error: any) {
        this.errorText = error
        this.openModal("error")
        return
      }
      this.closeModal("delete")
    },
    resetEditUser(): EditUser {
      return {
        name_changed: false,
        name: this.userStore.getName || "",
        email_changed: false,
        email: this.userStore.getEmail || "",
        dob_changed: false,
        dob: this.userStore.getDoB || "",
        password_changed: false,
        old_password: "",
        new_password: "",
        confirm_new_password: ""
      }
    },
    discardChanges() {
      // if the edit checkbox isn't checked, revert to default values (= discard changes made if there were any)
      if (!this.editUser.name_changed) {
        this.editUser.name = this.userStore.getName || ""
      }
      if (!this.editUser.email_changed) {
        this.editUser.email = this.userStore.getEmail || ""
      }
      if (!this.editUser.dob_changed) {
        this.editUser.dob = this.userStore.getDoB || ""
      }
      if (!this.editUser.password_changed) {
        this.editUser.old_password = ""
        this.editUser.new_password = ""
        this.editUser.confirm_new_password = ""
        this.showOldPassword = false
        this.showNewPassword = false
        this.showConfirmNewPassword = false
      }
    }
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
  }
})
</script>

<template>
  <div class="px-6 h-full flex flex-col items-center gap-6 overflow-y-auto">
    <h1 class="text-3xl font-semibold">My Profile</h1>
    <div class="card bg-base-100 min-w-96 shadow-xl ">
      <div class="card-body flex flex-col items-center ">
        <div :class="['w-32', 'h-32', 'rounded-full', getInitialBGColour(userStore?.getInitials || '')]">
          <div class="flex flex-row items-center justify-center h-full w-full">
            <span class="w-full text-center text-5xl font-semibold text-neutral-700">{{ userStore.getInitials }}</span>
          </div>
        </div>

        <div class="divider font-semibold text-neutral-400" id="display_name">{{ userStore.getName }}</div>
        <h2 class="text-md font-semibold text-neutral-400 self-start flex flex-row gap-2">
          <Mail/>
          <span id="display_email">
          {{ userStore.getEmail }}
            </span>
        </h2>
        <h2 class="text-md font-semibold text-neutral-400 self-start flex flex-row gap-2">
          <Calendar/>
          <span id="display_dob">
          {{ userStore.getDoB }}
          </span>
        </h2>

        <div class="divider font-semibold text-neutral-400">Hobbies</div>
        <button @click="openModal('add_hobby')"
                class="btn w-full mb-1"
                id="profile_add_hobby_modal">Add Hobby
        </button>
        <ul class="flex flex-col w-full gap-2">
          <div v-if="userStore.getHobbies?.length === 0 " class="text-center font-semibold text-neutral-400">No hobbies to display. <br> <i>Why not add some?</i> </div>
          <button v-else @click="deleteUserHobby(hobby.id)" v-for="hobby in userStore.getHobbies" :key="hobby.id"
                  class="w-full capitalize text-md font-semibold btn bg-slate-700 border-0 hover:bg-slate-500 text-white justify-between"
                  :id="`profile_displayed_hobby_${hobby.id}`">
            {{ hobby.name }}
            <Trash :size="16"/>
          </button>
        </ul>
        
        <!--
          Only displayed on mobile
          so that mobile users can
          accept/reject friend requests
          and see their friends list
        -->
        <div class="hidden max-md:flex flex-col w-full gap-2">
          <div class="divider font-semibold text-neutral-400">Friend Requests ({{ friendRequests.length }})</div>
          <ul class="flex flex-col gap-1 mb-4">
            <div v-if="friendRequests.length === 0 " class="text-center font-semibold text-neutral-400">No new friend requests. <br> <i>It's just a matter of time though!</i> </div>
            <div v-else v-for="request in friendRequests" :key="request.user1.id"
                class="capitalize text-md font-medium  bg-slate-700 rounded-lg flex flex-row p-2 px-4 text-white justify-between items-center">
              {{ request.user1.name }}
              <div class="flex flex-row-reverse items-center gap-1">
                <button @click="acceptFriendRequest(request.user1.id)"
                        class="btn bg-slate-500 hover:bg-slate-400 border-0 h-8 min-h-0 aspect-square p-0">
                  <Check :size="16" color="white"/>
                </button>
                <button @click="rejectFriendRequestOrRemoveFriend(request.user1.id)"
                        class="btn bg-slate-500 hover:bg-slate-400 border-0 h-8 min-h-0 aspect-square p-0">
                  <X :size="16" color="white"/>
                </button>
              </div>
            </div>
          </ul>

          <div class="divider font-semibold text-neutral-400">Friends ({{ friends.length }})</div>
          <div v-if="friends.length === 0 " class="text-center font-semibold text-neutral-400">No friends to display. <br> <i>Perfect time to make some!</i> </div>
          <ul v-else class="flex flex-col gap-1 mb-4">
            <a :href="'mailto:' + friend.email" v-for="friend in friends" :key="friend.id"
              class="capitalize text-md font-medium btn bg-slate-700 border-0 hover:bg-slate-500 text-white justify-between">
              {{ friend.name }}
              <Mail :size="16"/>
            </a>
          </ul>
        </div>

        <div class="divider font-semibold text-neutral-400">Settings</div>
        <div class="card-actions justify-end w-full pt-2">
          <button @click="openModal('edit')" class="btn w-full" id="edit">Edit Profile</button>
        </div>
        <div class="card-actions justify-end w-full pt-2">
          <button @click="openModal('delete')" class="btn btn-error w-full">Delete Account</button>
        </div>
      </div>
    </div>
  </div>

  <!--  Edit Profile Modal  -->
  <dialog id="edit_profile_modal" class="modal flex flex-row">
    <div class="w-1/6"/>
    <div class="flex-grow flex items-center justify-center">
      <div class="modal-box">
        <h3 class="font-bold text-lg">Edit Profile</h3>
        <form @submit.prevent="submitForm">

          <section class="form-control mb-4">
            <label class="label">Name</label>
            <div class="w-full flex flex-row-reverse items-center justify-between gap-2">
              <label class="btn btn-square swap swap-rotate" id="change_name">
                <input type="checkbox" name="change_name" v-model="editUser.name_changed" @click="discardChanges">
                <PencilLine class="swap-off" :size="32" :color="'gray'"/>
                <X class="swap-on" :size="32" :color="'gray'"/>
              </label>
              <input v-model="editUser.name" type="text" class="input input-bordered w-full" name="name" required
                     :disabled="!editUser.name_changed"/>
            </div>
          </section>

          <section class="form-control mb-4">
            <label class="label">Email</label>
            <div class="w-full flex flex-row-reverse items-center justify-between gap-2">
              <label class="btn btn-square swap swap-rotate" id="change_email">
                <input type="checkbox" name="change_email" v-model="editUser.email_changed" @click="discardChanges">
                <PencilLine class="swap-off" :size="32" :color="'gray'"/>
                <X class="swap-on" :size="32" :color="'gray'"/>
              </label>
              <input v-model="editUser.email" type="email" class="input input-bordered w-full" name="email" required
                     :disabled="!editUser.email_changed"/>
            </div>
          </section>

          <section class="form-control mb-4">
            <label class="label">Date of birth</label>
            <div class="w-full flex flex-row-reverse items-center justify-between gap-2">
              <label class="btn btn-square swap swap-rotate" id="change_dob">
                <input type="checkbox" name="change_dob" v-model="editUser.dob_changed" @click="discardChanges">
                <PencilLine class="swap-off" :size="32" :color="'gray'"/>
                <X class="swap-on" :size="32" :color="'gray'"/>
              </label>
              <input v-model="editUser.dob" :type="editUser.dob_changed ? 'date' : 'text'" class="input input-bordered w-full" name="dob" required
                     :disabled="!editUser.dob_changed"/>
            </div>
          </section>

          <section class="form-control mb-4">
            <label class="label">Password</label>
            <!--Div not a button to avoid auto submit :)-->
            <div class="w-full btn" id="edit_password"
                 @click="() => {editUser.password_changed = !editUser.password_changed; discardChanges()}">
              {{ editUser.password_changed ? 'Cancel' : 'Edit Password' }}
            </div>
          </section>

          <section v-if="editUser.password_changed">

            <div class="form-control mb-4">
              <label class="label">Old Password</label>
              <div class="w-full flex flex-row-reverse items-center justify-between gap-2">
                <label class="btn btn-square swap swap-rotate">
                  <input type="checkbox" name="change_old_pw" v-model="showOldPassword">
                  <EyeOff class="swap-off" :size="32" :color="'gray'"/>
                  <Eye class="swap-on" :size="32" :color="'gray'"/>
                </label>
                <input id="change_old_pw" name="old_pw" v-model="editUser.old_password" :type="showOldPassword ? 'text' : 'password'"
                       class="input input-bordered w-full" :disabled="!editUser.password_changed"/>
              </div>
            </div>
            <div class="form-control mb-4">
              <label class="label">New Password</label>
              <div class="w-full flex flex-row-reverse items-center justify-between gap-2">
                <label class="btn btn-square swap swap-rotate">
                  <input type="checkbox" name="change_new_pw" v-model="showNewPassword">
                  <EyeOff class="swap-off" :size="32" :color="'gray'"/>
                  <Eye class="swap-on" :size="32" :color="'gray'"/>
                </label>
                <input id="change_old_pw" name="pw" v-model="editUser.new_password" :type="showNewPassword ? 'text' : 'password'"
                       class="input input-bordered w-full" :disabled="!editUser.password_changed"/>
              </div>
            </div>
            <div class="form-control mb-4">
              <label class="label">Confirm New Password</label>
              <div class="w-full flex flex-row-reverse items-center justify-between gap-2">
                <label class="btn btn-square swap swap-rotate">
                  <input type="checkbox" name="cpw" v-model="showConfirmNewPassword">
                  <EyeOff class="swap-off" :size="32" :color="'gray'"/>
                  <Eye class="swap-on" :size="32" :color="'gray'"/>
                </label>
                <input id="change_confirm_new_password" name="cpw" v-model="editUser.confirm_new_password"
                       :type="showConfirmNewPassword ? 'text' : 'password'"
                       class="input input-bordered w-full" :disabled="!editUser.password_changed"/>
              </div>
            </div>
          </section>


          <div class="modal-action">
            <button type="submit" class="btn btn-success" id="save">Save</button>
            <button type="button" class="btn" @click="closeModal('edit')">Cancel</button>
          </div>
        </form>
      </div>
    </div>
  </dialog>

  <!--  Delete Profile Modal  -->
  <dialog id="delete_profile_modal" class="modal flex flex-row">
    <div class="w-1/6"/>
    <div class="flex-grow flex items-center justify-center">
      <div class="modal-box">
        <h3 class="text-lg font-semibold">Are you sure you wan to delete your account?</h3>
        <p class="py-4">This action is irreversible.</p>
        <div class="modal-action">
          <button class="btn btn-error" @click="onDelete">Delete Account</button>
          <button class="btn" @click="closeModal('delete')">Close</button>
        </div>
      </div>
    </div>
  </dialog>

  <!--  Error Profile Modal  -->
  <dialog id="error_profile_modal" class="modal flex flex-row">
    <div class="w-1/6"/>
    <div class="flex-grow flex items-center justify-center">
      <div class="modal-box">
        <h3 class="text-lg font-semibold text-error">Error</h3>
        <p class="py-4 text-error">{{ errorText }}</p>
        <div class="modal-action">
          <button class="btn" @click="closeModal('error')">Close</button>
        </div>
      </div>
    </div>
  </dialog>

  <!--  Add Hobby Modal  -->
  <dialog id="add_hobby_profile_modal" class="modal text-neutral-700" @close="closeModal('add_hobby')">
    <div class="modal-box min-w-[50vw]">
      <form method="dialog">
        <button class="btn btn-sm btn-circle btn-ghost absolute right-2 top-2">✕</button>

        <div class="flex w-full my-6">
          <div class="card rounded-box flex-grow place-items-center min-h-20 w-1/2 gap-6 mx-10">
            <h1>Select an Existing Hobby</h1>
            <select class="select select-bordered w-full max-w-xs" v-model="selectedHobby" id="profile_hobby_selector">
              <option selected disabled>Select a Hobby</option>
              <option v-for="hobby in hobbies" :key="hobby.id" :value="hobby.id" :id="`profile_select_hobby_${hobby.id}`">{{ hobby.name }}</option>
            </select>
            <button :class="['btn w-full', !selectedHobby && 'btn-disabled']"
                    @click="addUserHobby(hobbies.filter(h => h.id === selectedHobby)[0]?.name)"
                    id="profile_select_hobby_submit">
              Add Hobby
            </button>
          </div>

          <div class="divider divider-horizontal">OR</div>

          <div class="card rounded-box flex-grow place-items-center min-h-20 w-1/2 gap-6 mx-10">
            <h1>Add a New Hobby</h1>
            <input type="text" placeholder="Type here..." class="input input-bordered w-full max-w-xs"
                    v-model="typedHobby" id="profile_type_hobby"/>
            <button :class="['btn w-full', !typedHobby && 'btn-disabled']" @click="addUserHobby(typedHobby);" id="profile_type_hobby_submit">
              Add Hobby
            </button>
          </div>
        </div>
      </form>
    </div>
  </dialog>
</template>