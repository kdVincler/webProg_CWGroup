import {defineStore} from "pinia";
import {getUsersPaginated} from "../api.ts";
import {Hobby} from "./hobbies.ts";

export interface Page {
    current_page: number,
    total_pages: number,
    total_users: number,
    users: PaginatedUser[]
}

export interface PaginatedUser {
    id: number,
    name: string,
    age: number,
    hobbies: Hobby[],
    similar_hobbies_count: number
    similar_hobbies: Hobby[]
}

export const usePageStore = defineStore('page', {
    state: () => ({
        page: null as Page | null,
    }),
     actions: {
        async paginate(page_number: number, age_range?: { low: number, high: number }) {
            try {
                const ret = await getUsersPaginated(page_number, age_range)
                this.page = ret.page
            } catch (error: any) {
                console.log('Failed to paginate. Error:', error)
                this.page = null
            }
        }
     },
    getters: {
        getPage(): Page | undefined {
            return this.page || undefined
        },
        getCurrentPageNumber(): number | undefined {
            return this.page?.current_page
        },
        getTotalPages(): number | undefined {
            return this.page?.total_pages
        },
        getTotalUsers(): number | undefined {
            return this.page?.total_users
        },
        getUsers(): PaginatedUser[] | undefined {
            return this.page?.users
        }
    },
});