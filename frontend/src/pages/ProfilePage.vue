<template>
    <div class="profile-page flex flex-col justify-center items-center h-screen gap-2">
  
      <div class="profile-details">
        <h1 class="text-2xl font-bold mb-4">User Profile</h1>
        <p><strong>Name:</strong> {{ user.name }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Date of Birth:</strong> {{ user.dob }}</p>
        <p><strong>Hobbies:</strong> {{ user.hobbies.join(', ') }}</p>
        <button class="btn btn-primary mt-4" @click="openModal">Edit Profile</button>
      </div>
  
      <dialog id="profile_modal" class="modal">
        <div class="modal-box">
          <h3 class="font-bold text-lg">Edit Profile</h3>
          <form @submit.prevent="saveProfile">
            <div class="form-control mb-4">
              <label class="label">Name</label>
              <input v-model="editUser.name" type="text" class="input input-bordered" required />
            </div>
  
            <div class="form-control mb-4">
              <label class="label">Email</label>
              <input v-model="editUser.email" type="email" class="input input-bordered" required />
            </div>
  
            <div class="form-control mb-4">
              <label class="label">Date of Birth</label>
              <input v-model="editUser.dob" type="date" class="input input-bordered" required />
            </div>
  
            <div class="form-control mb-4">
              <label class="label">Hobbies</label>
              <input v-model="newHobby" type="text" class="input input-bordered mb-2" placeholder="Add a new hobby" />
              <button class="btn btn-secondary" type="button" @click="addHobby">Add Hobby</button>
              <ul class="mt-2">
                <li v-for="(hobby, index) in editUser.hobbies" :key="index" class="mb-2">
                  {{ hobby }}
                  <button class="btn btn-sm btn-error ml-2" @click.prevent="removeHobby(index)">Remove</button>
                </li>
              </ul>
            </div>
  
            <div class="form-control mb-4">
              <label class="label">Password</label>
              <div class="relative">
                <input v-model="editUser.password" :type="showPassword ? 'text' : 'password'" class="input input-bordered" />
                <button type="button" class="btn btn-sm absolute top-2 right-2" @click="toggleShowPassword">
                  {{ showPassword ? 'Hide' : 'Show' }}
                </button>
              </div>
            </div>
  
            <div class="modal-action">
              <button type="submit" class="btn btn-success">Save</button>
              <button type="button" class="btn" @click="closeModal">Cancel</button>
            </div>
          </form>
        </div>
      </dialog>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, reactive, ref } from 'vue';
  
  export default defineComponent({

    data() {
              return {
                  title: "Profile Page",
              }
          },

    name: 'ProfilePage',
    setup() {
      const user = reactive({
        name: 'John Doe',
        email: 'john.doe@example.com',
        dob: '1990-01-01',
        hobbies: ['Reading', 'Gaming'],
        password: ''
      });
  
      const editUser = reactive({ ...user });
      const newHobby = ref('');
      const showPassword = ref(false);
  
      const openModal = () => {
        (document.getElementById('profile_modal') as HTMLDialogElement).showModal();
      };
  
      const closeModal = () => {
        (document.getElementById('profile_modal') as HTMLDialogElement).close();
      };
  
      const saveProfile = () => {
        Object.assign(user, editUser);
        closeModal();
        // Placeholder for AJAX call
        // fetch('/api/update-profile', {
        //   method: 'POST',
        //   headers: { 'Content-Type': 'application/json' },
        //   body: JSON.stringify(user),
        // });
      };
  
      const addHobby = () => {
        if (newHobby.value.trim()) {
          editUser.hobbies.push(newHobby.value.trim());
          newHobby.value = '';
        }
      };
  
      const removeHobby = (index: number) => {
        editUser.hobbies.splice(index, 1);
      };
  
      const toggleShowPassword = () => {
        showPassword.value = !showPassword.value;
      };
  
      return {
        user,
        editUser,
        newHobby,
        showPassword,
        openModal,
        closeModal,
        saveProfile,
        addHobby,
        removeHobby,
        toggleShowPassword,
      };
    },
  });
  </script>
  
  <style scoped>
  .profile-page {
    padding: 20px;
  }
  .modal-box {
    max-width: 500px;
  }
  </style>
  


  