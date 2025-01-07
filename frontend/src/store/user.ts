import {defineStore} from "pinia";
import {checkAuthStatus} from "../api.ts";

export interface User {
    id: number;
    name: string;
    email: string;
}

export const useUserStore = defineStore('user', {
    state: () => ({
        authenticated: false,
        user: null as User | null,
    }),
     actions: {
         async fetchAuthStatus() {
             try {
                 const {authenticated, user} = await checkAuthStatus();
                 this.authenticated = authenticated || false;
                 this.user = user || null;
             } catch (error) {
                 console.error('Failed to fetch auth status:', error);
                 this.authenticated = false;
                 this.user = None;
             }
         },
     },
    getters: {
        isLoggedIn(): boolean {
            return !!this.user;
        },
        getName(): string | undefined {
            return this.user?.name;
        },
        getInitials(): string | undefined {
            return this.user?.name.split(' ').map((n) => n[0]).join('');
        }
    },
});