import { detectImage } from "../../services/detectionService";

export default function ImageUpload({ setResultImage }) {
    async function handleFileChange(event) {
        const file = event.target.files[0];
        if (!file) return;

        try {
            const resultUrl = await detectImage(file);
            setResultImage(resultUrl);
        } catch (error) {
            console.error('Error during detection:', error);
            alert('Detection failed. Please try again.');
        }
    }
    return (
    <input type="file" accept="image/*" onChange={handleFileChange}/>
    )
}