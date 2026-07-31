function JobDescription({ jobDescription, setJobDescription }) {
  return (
    <div style={styles.container}>
      <h2>Job Description</h2>

      <textarea
        placeholder="Paste the Job Description here..."
        rows="10"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        style={styles.textarea}
      />
    </div>
  );
}

const styles = {
  container: {
    marginBottom: "30px",
  },

  textarea: {
    width: "100%",
    padding: "15px",
    fontSize: "16px",
    borderRadius: "8px",
    border: "1px solid #ccc",
    resize: "vertical",
    boxSizing: "border-box",
  },
};

export default JobDescription;