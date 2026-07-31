function ResumeUpload({ resumes, setResumes }) {
  const handleFileChange = (event) => {
    setResumes(Array.from(event.target.files));
  };

  return (
    <div style={styles.container}>
      <h2>Upload Resumes</h2>

      <input
        type="file"
        multiple
        accept=".pdf,.doc,.docx"
        onChange={handleFileChange}
      />

      {resumes.length > 0 && (
        <div style={styles.fileList}>
          <h3>Selected Files:</h3>

          <ul>
            {resumes.map((resume, index) => (
              <li key={index}>📄 {resume.name}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    marginBottom: "30px",
  },

  fileList: {
    marginTop: "15px",
    padding: "10px",
    border: "1px solid #ddd",
    borderRadius: "8px",
    backgroundColor: "#f9f9f9",
  },
};

export default ResumeUpload;