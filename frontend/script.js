document.getElementById('upload-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const formData = new FormData();
    formData.append('file', document.getElementById('file-input').files[0]);

    try {
        const response = await fetch('https://your-backend-url/solve', {
            method: 'POST',
            body: formData,
        });

        if (!response.ok) {
            throw new Error('Failed to process the image');
        }

        const result = await response.json();
        document.getElementById('solution').innerText = `Best Moves: ${result.moves.join(', ')}`;
    } catch (error) {
        document.getElementById('solution').innerText = `Error: ${error.message}`;
    }
});
