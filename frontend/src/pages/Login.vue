<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
  name: "Log in to your account",
  data() {
    return {
        email: "",
        password: ""
    }
  },
  methods: {
    async handleLogin() {
        if (this.email === "" || this.password === "") {
            alert("Please fill out all fields")
            return
        } else if (!this.email.includes("@") || !this.email.includes(".")) {
            alert("Please provide a valid email address")
            this.email = ""
            return
        }
        try {
            const response = await fetch(``, {}) // placeholder
            if (response.ok) {
                // todo
                this.email, this.password = ""
            } else {
                alert(response.status + " " + response.statusText)
            }
        } catch (error) {
            alert("Error:" + error)
        }
        
    }
  }
})
</script>

<template>
    <div class="flex flex-col justify-center items-center h-screen gap-2">
        <label class="text-xl font-extrabold">
            Log in
        </label>
        <label class="input input-bordered flex items-center gap-2">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 16 16"
                fill="currentColor"
                class="h-4 w-4 opacity-70">
                <path
                d="M2.5 3A1.5 1.5 0 0 0 1 4.5v.793c.026.009.051.02.076.032L7.674 8.51c.206.1.446.1.652 0l6.598-3.185A.755.755 0 0 1 15 5.293V4.5A1.5 1.5 0 0 0 13.5 3h-11Z" />
                <path
                d="M15 6.954 8.978 9.86a2.25 2.25 0 0 1-1.956 0L1 6.954V11.5A1.5 1.5 0 0 0 2.5 13h11a1.5 1.5 0 0 0 1.5-1.5V6.954Z" />
            </svg>
            <input type="email" class="grow" placeholder="Email" v-model="email"/>
        </label>
        <label class="input input-bordered flex items-center gap-2">
            <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 16 16"
                fill="currentColor"
                class="h-4 w-4 opacity-70">
                <path
                fill-rule="evenodd"
                d="M14 6a4 4 0 0 1-4.899 3.899l-1.955 1.955a.5.5 0 0 1-.353.146H5v1.5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1-.5-.5v-2.293a.5.5 0 0 1 .146-.353l3.955-3.955A4 4 0 1 1 14 6Zm-4-2a.75.75 0 0 0 0 1.5.5.5 0 0 1 .5.5.75.75 0 0 0 1.5 0 2 2 0 0 0-2-2Z"
                clip-rule="evenodd" />
            </svg>
            <input type="password" class="grow" placeholder="Password" v-model="password"/>
        </label>
        <RouterLink to="/register" class="btn-link"> Do not have an account? Register</RouterLink>
        <button class="btn btn-md" @click="handleLogin">Log in</button>
    </div>
</template>

<style scoped>

</style>