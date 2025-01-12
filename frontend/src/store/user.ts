import {defineStore} from "pinia";
import {checkAuthStatus, getFriendRequests, getFriends} from "../api.ts";
import {Hobby} from "./hobbies.ts";

export interface User {
    id: number;
    name: string;
    email: string;
    date_of_birth: string;
    hobbies: Hobby[];
}

export interface Friend {
    id: number;
    user1: {
        id: number;
        username: string;
        name: string
    };
    user2: {
        id: number;
        username: string;
        name: string
    };
    accepted: boolean
}

export interface FriendRequests {
    incoming_requests: Friend[];
    outgoing_requests: Friend[];
}

export const useUserStore = defineStore('user', {
    state: () => ({
        authenticated: false,
        user: null as User | null,
        friends: null as User[] | null,
        friend_requests: null as FriendRequests | null
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
         async updateFriendRequests() {
            // get user's friends requests
            try {
                const ret = await getFriendRequests();
                this.friend_requests = ret || null
            } catch (error) {
                console.error('Failed to fetch friend requests. Error: ', error);
                this.friend_requests = null
            }
            // get user's friends
            try {
                const ret = await getFriends();
                this.friends = ret.friends || null
            } catch (error) {
                console.error('Failed to fetch friends. Error: ', error);
                this.friends = null
            }
         }
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
        getHobbies(): Hobby[] | undefined {
            return this.user?.hobbies;
        },
        getUserFriends(): User[] | undefined {
            return this.friends || undefined
        },
        getOutgoingFriendRequests(): Friend[] | undefined {
            return this.friend_requests?.outgoing_requests
        },
        getIncomingFriendRequests(): Friend[] | undefined {
            return this.friend_requests?.incoming_requests
        }
    },
});