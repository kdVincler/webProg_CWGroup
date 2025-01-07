import {defineStore} from "pinia";
import {checkAuthStatus} from "../api.ts";

export interface User {
    id: number;
    name: string;
    email: string;
    date_of_birth: string;
    hobbies: string[];
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
                 if (!authenticated) {
                        window.location.href = 'http://localhost:8000/login';
                 }
                 this.authenticated = authenticated || false;
                 this.user = user || null;
             } catch (error) {
                 console.error('Failed to fetch auth status:', error);
                 this.authenticated = false;
                 this.user = null;
             }
         },
     },
    getters: {
        isLoggedIn(): boolean {
            return this.authenticated;
        },
        getName(): string | undefined {
            return this.user?.name;
        },
        getInitials(): string | undefined {
            return this.user?.name.split(' ').map((n) => n[0]).join('');
        },
        getEmail(): string | undefined {
            return this.user?.email;
        },
        getDoB(): string | undefined {
            return this.user?.date_of_birth;
        },
        getHobbies(): string[] | undefined {
            return this.user?.hobbies;
        }
    },
});