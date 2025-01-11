import {Friend, FriendRequests, User, useUserStore} from "./store/user.ts";
import { useHobbiesStore, Hobby } from "./store/hobbies.ts";
import { usePageStore, Page } from "./store/page.ts";

export interface EditUser {
    name_changed: boolean;
    name: string;
    email_changed: boolean;
    email: string;
    dob_changed: boolean;
    dob: string;
    password_changed: boolean;
    old_password: string;
    new_password: string;
    confirm_new_password: string;
}

function getCSRFToken(): string | null {
    const csrfCookie = document.cookie
        .split('; ')
        .find((row) => row.startsWith('csrftoken='));
    return csrfCookie ? csrfCookie.split('=')[1] : null;
}

const getUsersPaginated = async (page_number: number, age_range?: { low: number, high: number }): Promise<{
    page: Page
}> => {
    let response;
    if (!age_range) {
        response = await fetch(`http://localhost:8000/users/page/${page_number}/`, {
            method: 'GET',
            credentials: 'include'
        });
    } else {
        response = await fetch(`http://localhost:8000/users/page/${page_number}/?age_low=${age_range.low}&age_high=${age_range.high}`, {
            method: 'GET',
            credentials: 'include'
        });
    }
    if (!response.ok) {
        throw new Error('Failed to fetch page of users');
    }
    const data = await response.json();
    return data;
}

const logout = async (): Promise<void> => {
    try {
        const response = await fetch(
            'http://localhost:8000/logout/',
            {
                method: 'GET',
                credentials: 'include',
            }
        )

        if (!response.ok) {
            alert("Logout unsuccessful, try again")
        } else {
            window.location.href = 'http://localhost:8000/login';

        }
    } catch (error: any) {
        alert("Error: " + error)
    }
}

const updateUser = async (edited_user: EditUser) => {
    const response = await fetch('http://localhost:8000/user/',
        {
            method: 'PUT',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken() || '',
            },
            body: JSON.stringify({
                name_changed: edited_user.name_changed,
                name: edited_user.name,
                email_changed: edited_user.email_changed,
                email: edited_user.email,
                dob_changed: edited_user.dob_changed,
                dob: edited_user.dob,
                password_changed: edited_user.password_changed,
                old_password: edited_user.old_password,
                new_password: edited_user.new_password,
            })
        }
    );
    if (!response.ok) {
        throw new Error(`Failed to edit profile. Reason: ${response.status} - ${response.statusText}`);
    }
    await useUserStore().fetchAuthStatus();
}

const deleteUser = async () => {
    const response = await fetch('http://localhost:8000/user/',
        {
            method: 'DELETE',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken() || '',
            },
        }
    );
    if (!response.ok) {
        throw new Error(`Failed to delete account. Reason: ${response.status} - ${response.statusText}`);
    }
    await useUserStore().fetchAuthStatus();
}

const addUserHobby = async (name: String): Promise<void> => {
    const response = await fetch('http://localhost:8000/user-hobby/',
        {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken() || '',
            },
            body: JSON.stringify({name: name})
        }
    );
    if (!response.ok) {
        throw new Error('Failed to add hobby');
    }
    useUserStore().fetchAuthStatus();
    useHobbiesStore().populate(); // needs to update the list in the store so sidebar updates
    usePageStore().paginate(1); // needs to update the page from the start, as the new hobby list could mess with the order
}

const deleteUserHobby = async (id: Number): Promise<void> => {
    const response = await fetch(`http://localhost:8000/user-hobby/${id}/`,
        {
            method: 'DELETE',
            credentials: 'include',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCSRFToken() || '',
            },
        }
    );
    if (!response.ok) {
        throw new Error('Failed to delete hobby');
    }
    useUserStore().fetchAuthStatus();
    usePageStore().paginate(1); // needs to update the page from the start, as the new hobby list could mess with the order
}

export async function fetchAllHobbies(): Promise<{ hobbies: Hobby[] }> {
    const response = await fetch('http://localhost:8000/hobby/', {
        method: 'GET',
        credentials: 'include'
    });
    if (!response.ok) {
        throw new Error('Failed to fetch hobbies list');
    }
    const data = await response.json();
    return data;
}

export async function acceptFriendRequest(id: number): Promise<void> {
    const response = await fetch(`http://localhost:8000/accept-friend-request/${id}/`, {
        method: 'POST',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() || '',
        }
    });
    if (!response.ok) {
        throw new Error('Failed to accept friend request');
    }
    useUserStore().updateFriendRequests();
}

export async function rejectFriendRequestOrRemoveFriend(id: number): Promise<void> {
    const response = await fetch(`http://localhost:8000/reject-friend-request/${id}/`, {
        method: 'DELETE',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() || '',
        }
    });
    if (!response.ok) {
        throw new Error('Failed to reject friend request');
    }
    useUserStore().updateFriendRequests();
}

export async function sendFriendRequest(id: number): Promise<void> {
    const response = await fetch(`http://localhost:8000/send-friend-request/${id}/`, {
        method: 'POST',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken() || '',
        }
    });
    if (!response.ok) {
        throw new Error('Failed to send friend request');
    }
    useUserStore().updateFriendRequests();
}

export async function getFriends(): Promise<{friends: Friend[]}> {
    const response = await fetch(`http://localhost:8000/friends/`, {
        method: 'GET',
        credentials: 'include',
        headers: {
            'Content-Type': 'application/json',
        }
    });
    if (!response.ok) {
        throw new Error('Failed to get friends');
    }
    const data = await response.json();
    return data;
}

export async function getFriendRequests(): Promise<FriendRequests> {
    const response = await fetch('http://localhost:8000/friend-requests/', {
        method: 'GET',
        credentials: 'include'
    });
    if (!response.ok) {
        throw new Error('Failed to fetch friend requests');
    }
    const data = await response.json();
    return data;
}


export async function checkAuthStatus(): Promise<{ authenticated: boolean; user: User }> {
    const response = await fetch('http://localhost:8000/auth-status', {
        credentials: 'include',
    });
    if (!response.ok) {
        throw new Error('Failed to fetch authentication status');
    }
    return response.json();
}

export {getUsersPaginated, logout, updateUser, deleteUser, addUserHobby, deleteUserHobby}