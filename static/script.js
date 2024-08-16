document.getElementById('uploadForm').onsubmit = async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const response = await fetch('/upload', {
        method: 'POST',
        body: formData
    });
    const result = await response.json();
    document.getElementById('output').textContent = result.text;
};
