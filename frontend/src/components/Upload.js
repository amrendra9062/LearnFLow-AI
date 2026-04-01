import axios from "axios";

function Upload({ setData }) {

  const handlePDF = async (e) => {
    try {
      const formData = new FormData();
      formData.append("file", e.target.files[0]);

      const res = await axios.post(
        "http://localhost:8000/upload/pdf",
        formData
      );

      setData(res.data);
    } catch (err) {
      alert("Error uploading file");
    }
  };

  const handleYouTube = async () => {
    const url = prompt("Enter YouTube URL");

    try {
      const res = await axios.post(
        "http://localhost:8000/youtube",
        { url }
      );

      setData(res.data);
    } catch (err) {
      alert("Error fetching video");
    }
  };

  return (
    <div>
      <h2>Upload Content</h2>

      <input type="file" onChange={handlePDF} />

      <br /><br />

      <button onClick={handleYouTube}>Add YouTube Link</button>
    </div>
  );
}

export default Upload;