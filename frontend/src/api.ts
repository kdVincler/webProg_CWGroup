import {User} from "./store/user.ts";

const getUsers = async () => {
    const response = await fetch('http://localhost:8000/api/users');
    return await response.json();
}

const getUser = async (id: number) => {
    const response = await fetch(`http://localhost:8000/api/users/${id}`);
    return await response.json();
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

export { getUsers, getUser, createUser, updateUser, deleteUser }