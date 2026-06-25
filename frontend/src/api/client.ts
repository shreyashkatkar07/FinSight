const API_BASE_URL =
    "http://localhost:8000/api";

async function request<T>(
    url: string,
    options?: RequestInit,
): Promise<T> {
    const response = await fetch(
        `${API_BASE_URL}${url}`,
        {
            headers: {
                "Content-Type":
                    "application/json",
            },
            ...options,
        },
    );

    if (!response.ok) {
        throw new Error(
            `HTTP ${response.status}`
        );
    }

    return response.json();
}

export function get<T>(
    url: string,
) {
    return request<T>(url);
}

export function post<T>(
    url: string,
    body: unknown,
) {
    return request<T>(url, {
        method: "POST",
        body: JSON.stringify(body),
    });
}