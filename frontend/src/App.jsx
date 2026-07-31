import { useState } from "react";

import Header from "./components/Header";
import JobDescription from "./components/JobDescription";
import ResumeUpload from "./components/ResumeUpload";
import ResultsTable from "./components/ResultsTable";
import api from "./services/api";

function App() {
  const [jobDescription, setJobDescription] = useState("");
  const [resumes, setResumes] = useState([]);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleScreenCandidates = async () => {
    if (!jobDescription.trim()) {
      alert("Please enter a Job Description.");
      return;
    }

    if (resumes.length === 0) {
      alert("Please upload at least one resume.");
      return;
    }

    const formData = new FormData();

    formData.append("job_description", jobDescription);

    resumes.forEach((resume) => {
      formData.append("resumes", resume);
    });

    try {
      setLoading(true);

      const response = await api.post("/screen/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      console.log("Response:", response);
      console.log("Response Data:", response.data);

      setResults(response.data.results);
    } catch (error) {
      console.error("Complete Error:", error);

      if (error.response) {
        console.log("Status:", error.response.status);
        console.log("Data:", error.response.data);

        alert(
          `Error ${error.response.status}: ${JSON.stringify(
            error.response.data
          )}`
        );
      } else {
        alert(error.message);
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      style={{
        maxWidth: "1000px",
        margin: "30px auto",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
      }}
    >
      <Header />

      <JobDescription
        jobDescription={jobDescription}
        setJobDescription={setJobDescription}
      />

      <ResumeUpload
        resumes={resumes}
        setResumes={setResumes}
      />

      <div style={{ textAlign: "center", marginBottom: "30px" }}>
        <button
          onClick={handleScreenCandidates}
          disabled={loading}
          style={{
            padding: "15px 30px",
            fontSize: "18px",
            backgroundColor: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "8px",
            cursor: loading ? "not-allowed" : "pointer",
          }}
        >
          {loading ? "Screening..." : "🚀 Screen Candidates"}
        </button>
      </div>

      <ResultsTable results={results} />
    </div>
  );
}

export default App;