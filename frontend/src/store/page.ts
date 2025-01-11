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
        filter: undefined as { low: number, high: number } | undefined,
        filterEnabled: false
    }),
     actions: {
        async paginate(page_number: number) {
            try {
                
                const ret = this.filterEnabled ? await getUsersPaginated(page_number, this.filter) : await getUsersPaginated(page_number)
                this.page = ret.page
            } catch (error: any) {
                console.log('Failed to paginate. Error:', error)
                this.page = null
            }
        },
        async setFilter(filter: { low: number, high: number }) {
            this.filter = filter
            this.filterEnabled = true
            this.paginate(1)
        },
        async clearFilter() {
            this.filter = undefined
            this.filterEnabled = false
            this.paginate(1)
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
        },
        getFilter(): { low: number, high: number } | undefined {
            return this.filter
        },
        isFilterEnabled(): boolean {
            return this.filterEnabled
        }
    },
});