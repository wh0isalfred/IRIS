const API_BASE = 'http://localhost:8000';

export async function detectImage(imageFile){
    const formData = new FormData();
    formData.append('file', imageFile);

    const response = await fetch(`${API_BASE}/detect`, {
        method: 'POST',
        body: formData
    });

    if (!response.ok) {
  throw new Error(`Detection failed: ${response.status}`)
}

    const blob = await response.blob()
    return URL.createObjectURL(blob)
}