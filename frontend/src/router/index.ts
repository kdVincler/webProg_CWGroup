// Example of how to use Vue Router

import { createRouter, createWebHistory } from 'vue-router'

// 1. Define route components.
// These can be imported from other files
import MainPage from '../pages/MainPage.vue';
import OtherPage from '../pages/OtherPage.vue';
import Roman from '../pages/Roman.vue';
import Konrad from "../pages/Konrad.vue";
import Gabi from "../pages/Gabi.vue";
import Alicia from "../pages/Alicia.vue";

let base = (import.meta.env.MODE == 'development') ? import.meta.env.BASE_URL : ''

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const router = createRouter({
    history: createWebHistory(base),
    routes: [
        { path: '/', name: 'Main Page', component: MainPage },
        { path: '/other/', name: 'Other Page', component: OtherPage },
        { path: '/roman/', name: 'Roman Development', component: Roman },
        { path: '/konrad/', name: 'Konrad Development', component: Konrad },
        { path: '/gabi/', name: 'Gabi Development', component: Gabi},
        { path: '/alicia/', name: 'Alicia Development', component: Alicia},

    ]
})

export default router
