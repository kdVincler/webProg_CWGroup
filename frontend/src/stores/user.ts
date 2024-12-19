import {defineStore} from "pinia";

export interface User {
    id: number;
    name: string;
    email: string;
}

export const useUserStore = defineStore('user', {
    state: () => ({
        user: null as User | null,
    }),
    actions: {
        setUser(user: User) {
            this.user = user;
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