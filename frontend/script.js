document.getElementById("uploadForm").addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the form from submitting normally

    const fileInput = document.getElementById("fileInput");
    if (fileInput.files.length === 0) {
        alert("Please select a file.");
        return;
    }

    // Create FormData to hold the file
    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        // Make a POST request to the backend
        const response = await fetch("https://block-blast-solver-1.onrender.com/solve", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        // Parse the JSON response
        const data = await response.json();
        document.getElementById("result").textContent = JSON.stringify(data.moves, null, 2);
    } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
        alert("Failed to get a response from the server. Please try again later.");
    }
});
