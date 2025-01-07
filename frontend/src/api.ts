import {User} from "./store/user.ts";
import { Hobby } from "./store/hobbies.ts";

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

const getUserHobbies = async (): Promise<{ hobbies: Hobby[] }> => { 
    const response = await fetch('http://localhost:8000/user-hobby/',
        {
            method: 'GET',
            credentials: 'include'
        }
    );
    if (!response.ok) {
        throw new Error("Failed to get the user's hobbies");
    }
    return response.json()
}

const addUserHObby = async (name: String, description: String): Promise<void> => { 
    const response = await fetch('http://localhost:8000/user-hobby/',
        {
            method: 'POST',
            credentials: 'include',
            body: JSON.stringify({name: name, description: description})
        }
    );
    if (!response.ok) {
        throw new Error('Failed to add hobby');
    }
}


export async function checkAuthStatus(): Promise<{ authenticated: boolean; user: User }> {
    const response = await fetch('http://localhost:8000/auth-status', {
        credentials: 'include',
    });
    if (!response.ok) {
        throw new Error('Failed to fetch authentication status');
    }

    // if the user is not authenticated, redirect to the login page
    if (response.status !== 200) {
        window.location.href = 'http://localhost:8000/login';
    }
    return response.json();
}

export async function fetchAllHobbies(): Promise<{ hobbies: Hobby[] }> {
    const response = await fetch('http://localhost:8000/hobby/',
        {
            method: 'GET',
            credentials: 'include'
        }
    );
    if (!response.ok) {
        throw new Error('Failed to fetch hobbies list');
    }
    return response.json()
}

export {getUsers, getUser, logout, createUser, updateUser, deleteUser, getUserHobbies, addUserHObby}