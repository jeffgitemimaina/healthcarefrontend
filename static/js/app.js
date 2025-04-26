console.log("app.js loaded");

function showAlert(message, isError = false) {
    const alertDiv = document.createElement("div");
    alertDiv.className = `alert ${isError ? "alert-danger" : "alert-success"}`;
    alertDiv.textContent = message;
    document.body.appendChild(alertDiv);
    setTimeout(() => alertDiv.remove(), 3000);
}

function handleApiError(response) {
    if (!response.ok) {
        throw new Error(`API error: ${response.status} ${response.statusText}`);
    }
    return response.json();
}