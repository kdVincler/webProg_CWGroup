import {User, useUserStore} from "./store/user.ts";

export interface Hobby {
    id: number;
    name: string;
}

function getCSRFToken(): string | null {
    const csrfCookie = document.cookie
        .split('; ')
        .find((row) => row.startsWith('csrftoken='));
    return csrfCookie ? csrfCookie.split('=')[1] : null;
}


const getUsers = async () => {
    const response = await fetch('http://localhost:8000/api/users');
    return await response.json();
}

const getUser = async (id: number) => {
    const response = await fetch(`http://localhost:8000/api/users/${id}`);
    return await response.json();
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

const createUser = async (user: User) => {
    // Needs URL Gabi
    console.log(user);
}

const updateUser = async (id: number, user: User) => {
    // Needs URL Gabi
    console.log(id, user);
}

const deleteUser = async (id: number) => {
    // Needs URL Gabi
    console.log(id);
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


export async function checkAuthStatus(): Promise<{ authenticated: boolean; user: User }> {
    const response = await fetch('http://localhost:8000/auth-status', {
        credentials: 'include',
    });
    if (!response.ok) {
        throw new Error('Failed to fetch authentication status');
    }
    return response.json();
}

export {getUsers, getUser, logout, createUser, updateUser, deleteUser, addUserHobby, deleteUserHobby}