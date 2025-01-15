import {FriendRequests, User, useUserStore} from "./store/user.ts";
import {useHobbiesStore, Hobby} from "./store/hobbies.ts";
import {usePageStore, Page} from "./store/page.ts";

export let url = "";
if (import.meta.env.VITE_DEV_MODE === "true") {
    url = "http://localhost:8000";
}

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
        .split("; ")
        .find((row) => row.startsWith("csrftoken="));
    return csrfCookie ? csrfCookie.split("=")[1] : null;
}

const getUsersPaginated = async (
    page_number: number,
    age_range?: { low: number; high: number }
): Promise<{page: Page} | Error> => {
    let response;
    if (!age_range) {
        response = await fetch(`${url}/users/page/${page_number}/`, {
            method: "GET",
            credentials: "include",
        });
    } else {
        response = await fetch(
            `${url}/users/page/${page_number}/?age_low=${age_range.low}&age_high=${age_range.high}`,
            {
                method: "GET",
                credentials: "include",
            }
        );
    }
    if (!response.ok) {
        throw new Error("Failed to fetch page of users");
    }
    const data = await response.json();
    return data;
};

const logout = async (): Promise<void> => {
    try {
        const response = await fetch(`${url}/logout/`, {
            method: "GET",
            credentials: "include",
        });

        if (!response.ok) {
            alert("Logout unsuccessful, try again");
        } else {
            window.location.href = `${url}/login`;
        }
    } catch (error: any) {
        alert("Error: " + error);
    }
};

const updateUser = async (edited_user: EditUser): Promise<void | Error> => {
    const response = await fetch(`${url}/user/`, {
        method: "PUT",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken() || "",
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
        }),
    });
    if (!response.ok) {
        throw new Error(
            `Failed to edit profile. Reason: ${response.status} - ${response.statusText}`
        );
    }
    await useUserStore().fetchAuthStatus();
};

const deleteUser = async (): Promise<void | Error> => {
    const response = await fetch(`${url}/user/`, {
        method: "DELETE",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken() || "",
        },
    });
    if (!response.ok) {
        throw new Error(
            `Failed to delete account. Reason: ${response.status} - ${response.statusText}`
        );
    }
    await useUserStore().fetchAuthStatus();
};

const addUserHobby = async (name: String): Promise<void | Error> => {
    const response = await fetch(`${url}/user-hobby/`, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken() || "",
        },
        body: JSON.stringify({name: name}),
    });
    if (!response.ok) {
        throw new Error("Failed to add hobby");
    }
    useUserStore().fetchAuthStatus();
    useHobbiesStore().populate(); // needs to update the list in the store so sidebar updates
    usePageStore().paginate(1); // needs to update the page from the start, as the new hobby list could mess with the order
};

const deleteUserHobby = async (id: Number): Promise<void | Error> => {
    const response = await fetch(`${url}/user-hobby/${id}/`, {
        method: "DELETE",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken() || "",
        },
    });
    if (!response.ok) {
        throw new Error("Failed to delete hobby");
    }
    useUserStore().fetchAuthStatus();
    usePageStore().paginate(1); // needs to update the page from the start, as the new hobby list could mess with the order
};

export async function fetchAllHobbies(): Promise<{ hobbies: Hobby[] } | Error> {
    const response = await fetch(`${url}/hobby/`, {
        method: "GET",
        credentials: "include",
    });
    if (!response.ok) {
        throw new Error("Failed to fetch hobbies list");
    }
    const data = await response.json();
    return data;
}

export async function acceptFriendRequest(id: number): Promise<void | Error> {
    const response = await fetch(
        `${url}/accept-friend-request/${id}/`,
        {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken() || "",
            },
        }
    );
    if (!response.ok) {
        throw new Error("Failed to accept friend request");
    }
    useUserStore().updateFriendRequests();
}

export async function rejectFriendRequestOrRemoveFriend(
    id: number
): Promise<void | Error> {
    const response = await fetch(
        `${url}/reject-friend-request/${id}/`,
        {
            method: "DELETE",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken() || "",
            },
        }
    );
    if (!response.ok) {
        throw new Error("Failed to reject friend request");
    }
    useUserStore().updateFriendRequests();
}

export async function sendFriendRequest(id: number): Promise<void | Error> {
    const response = await fetch(
        `${url}/send-friend-request/${id}/`,
        {
            method: "POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCSRFToken() || "",
            },
        }
    );
    if (!response.ok) {
        throw new Error("Failed to send friend request");
    }
    useUserStore().updateFriendRequests();
}

export async function getFriends(): Promise<{ friends: User[] } | Error> {
    const response = await fetch(`${url}/friends/`, {
        method: "GET",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
        },
    });
    if (!response.ok) {
        throw new Error("Failed to get friends");
    }
    const data = await response.json();
    return data;
}

export async function getFriendRequests(): Promise<FriendRequests | Error> {
    const response = await fetch(`${url}/friend-requests/`, {
        method: "GET",
        credentials: "include",
    });
    if (!response.ok) {
        throw new Error("Failed to fetch friend requests");
    }
    const data = await response.json();
    return data;
}

export async function checkAuthStatus(): Promise<{
    authenticated: boolean;
    user: User;
} | Error> {
    const response = await fetch(`${url}/auth-status`, {
        credentials: "include",
    });
    if (!response.ok) {
        throw new Error("Failed to fetch authentication status");
    }
    return response.json();
}

export {
    getUsersPaginated,
    logout,
    updateUser,
    deleteUser,
    addUserHobby,
    deleteUserHobby,
};
