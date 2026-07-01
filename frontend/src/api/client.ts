const API_BASE_URL =
  "http://localhost:8000/api";

async function request<T>(
  url: string,
  options?: RequestInit,
): Promise<T> {
  const response = await fetch(
    `${API_BASE_URL}${url}`,
    options,
  );

  if (!response.ok) {
    throw new Error(
      `HTTP ${response.status}`,
    );
  }

  return response.json();
}

export function get<T>(
  url: string,
) {
  return request<T>(url, {
    method: "GET",
  });
}

export function postJson<T>(
  url: string,
  body: unknown,
) {
  return request<T>(url, {
    method: "POST",
    headers: {
      "Content-Type":
        "application/json",
    },
    body: JSON.stringify(body),
  });
}

export function postForm<T>(
  url: string,
  formData: FormData,
) {
  return request<T>(url, {
    method: "POST",
    body: formData,
  });
}

export function putJson<T>(
  url: string,
  body: unknown,
) {
  return request<T>(url, {
    method: "PUT",
    headers: {
      "Content-Type":
        "application/json",
    },
    body: JSON.stringify(body),
  });
}

export function deleteRequest<T>(
  url: string,
) {
  return request<T>(url, {
    method: "DELETE",
  });
}