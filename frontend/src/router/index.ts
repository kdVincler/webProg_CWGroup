// Example of how to use Vue Router

import { createRouter, createWebHistory } from 'vue-router'

import MainPage from '../pages/MainPage.vue';
import ProfilePage from '../pages/ProfilePage.vue';

let base = (import.meta.env.MODE == 'development') ? import.meta.env.BASE_URL : ''

const router = createRouter({
    history: createWebHistory(base),
    routes: [
        { path: '/', name: 'Main Page', component: MainPage },
        { path: '/profile', name: 'Profile Page', component: ProfilePage },
    ]
})


export default router
