import {defineStore} from "pinia";
import {fetchAllHobbies} from "../api.ts";

export interface Hobby {
    id: number;
    name: string;
    description: string;
}

export const useHobbiesStore = defineStore('hobbies', {
    state: () => ({
        hobbies: null as Hobby[] | null,
    }),
     actions: {
        async populate() {
            const ret = await fetchAllHobbies()
            this.hobbies = ret.hobbies || null
        }
     },
    getters: {
        getAllHobbies(): Hobby[] | null {
            return this.hobbies;
        },
    },
});