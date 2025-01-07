import {User} from "./store/user.ts";

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

export async function checkAuthStatus(): Promise<{ authenticated: boolean; user: User }> {
    const response = await fetch('http://localhost:8000/auth-status', {
        credentials: 'include',
    });
    if (!response.ok) {
        throw new Error('Failed to fetch authentication status');
    }
    return response.json();
}

export { getUsers, getUser, logout, createUser, updateUser, deleteUser }