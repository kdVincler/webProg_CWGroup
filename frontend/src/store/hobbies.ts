import {defineStore} from "pinia";
import {fetchAllHobbies} from "../api.ts";

export interface Hobby {
    id: number;
    name: string;
}

export const useHobbiesStore = defineStore('hobbies', {
    state: () => ({
        hobbies: null as Hobby[] | null,
    }),
     actions: {
        async populate() {
            try {
                const ret = await fetchAllHobbies()
                this.hobbies = ret.hobbies || null
            } catch (error: any) {
                console.log('Failed to fetch hobby list. Error:', error)
                this.hobbies = null
            }
        }
     },
    getters: {
        getAllHobbies(): Hobby[] | undefined {
            return this.hobbies || undefined;
        },
    },
});