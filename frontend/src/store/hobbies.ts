import {defineStore} from "pinia";
import {fetchAllHobbies, Hobby} from "../api.ts";

export const useHobbiesStore = defineStore('hobbies', {
    state: () => ({
        hobbies: null as Hobby[] | null,
    }),
     actions: {
        async populate() {
            try {
                console.log('hobbies populated')
                const ret = await fetchAllHobbies()
                this.hobbies = ret.hobbies || null
            } catch (error: any) {
                console.log(error)
                this.hobbies = null
            }
        }
     },
    getters: {
        getAllHobbies(): Hobby[] | null {
            return this.hobbies;
        },
    },
});