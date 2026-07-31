function ResultsTable({ results }) {
  // Helper function for decision badges
  const getDecisionStyle = (decision) => {
    switch (decision?.toLowerCase()) {
      case "shortlist":
        return { bg: "#dcfce7", text: "#15803d", border: "#bbf7d0" };
      case "partial match":
        return { bg: "#fef3c7", text: "#b45309", border: "#fde68a" };
      case "reject":
        return { bg: "#fee2e2", text: "#b91c1c", border: "#fecaca" };
      default:
        return { bg: "#f3f4f6", text: "#374151", border: "#e5e7eb" };
    }
  };

  return (
    <div style={{
      overflowX: "auto",
      marginTop: "30px",
      backgroundColor: "#ffffff",
      borderRadius: "12px",
      boxShadow: "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
      border: "1px solid #e5e7eb"
    }}>
      <table style={{ width: "100%", borderCollapse: "collapse", textAlign: "left" }}>
        <thead>
          <tr style={{ backgroundColor: "#f9fafb", borderBottom: "1px solid #e5e7eb" }}>
            <th style={{ padding: "16px 24px", color: "#6b7280", fontWeight: "600", fontSize: "14px", textTransform: "uppercase", letterSpacing: "0.05em" }}>Candidate File</th>
            <th style={{ padding: "16px 24px", color: "#6b7280", fontWeight: "600", fontSize: "14px", textTransform: "uppercase", letterSpacing: "0.05em" }}>Match Score</th>
            <th style={{ padding: "16px 24px", color: "#6b7280", fontWeight: "600", fontSize: "14px", textTransform: "uppercase", letterSpacing: "0.05em" }}>Decision</th>
            <th style={{ padding: "16px 24px", color: "#6b7280", fontWeight: "600", fontSize: "14px", textTransform: "uppercase", letterSpacing: "0.05em" }}>Summary & Feedback</th>
          </tr>
        </thead>
        <tbody>
          {results.map((result, index) => {
            const rec = result.recommendation || {};
            const evalData = rec.evaluation || {};
            const style = getDecisionStyle(rec.final_decision);
            const isLast = index === results.length - 1;

            return (
              <tr key={index} style={{ borderBottom: isLast ? "none" : "1px solid #e5e7eb" }}>

                {/* Filename */}
                <td style={{ padding: "24px", verticalAlign: "top" }}>
                  <div style={{ fontWeight: "600", color: "#111827", fontSize: "15px" }}>
                    {result.candidate || `Candidate ${index + 1}`}
                  </div>
                </td>

                {/* Semantic Score */}
                <td style={{ padding: "24px", verticalAlign: "top" }}>
                  <div style={{ fontWeight: "700", color: "#3b82f6", fontSize: "18px" }}>
                    {result.score ? `${result.score.toFixed(1)}%` : "N/A"}
                  </div>
                </td>

                {/* Final Decision Badge */}
                <td style={{ padding: "24px", verticalAlign: "top" }}>
                  <span style={{
                    backgroundColor: style.bg,
                    color: style.text,
                    border: `1px solid ${style.border}`,
                    padding: "6px 14px",
                    borderRadius: "9999px",
                    fontWeight: "600",
                    fontSize: "13px",
                    display: "inline-block",
                    textTransform: "capitalize"
                  }}>
                    {rec.final_decision || "Unknown"}
                  </span>
                </td>

                {/* Detailed Evaluation */}
                <td style={{ padding: "24px", verticalAlign: "top", fontSize: "14px", color: "#4b5563", lineHeight: "1.6" }}>

                  {/* Summary Text */}
                  <div style={{ marginBottom: "16px" }}>
                    <strong style={{ color: "#111827" }}>Summary:</strong> {rec.recommendation_summary}
                  </div>

                  <div style={{ display: "flex", flexDirection: "column", gap: "12px" }}>

                    {/* Render Missing Mandatory Requirements */}
                    {evalData.missing_mandatory_requirements?.length > 0 && (
                      <div style={{ backgroundColor: "#fef2f2", border: "1px solid #fecaca", padding: "12px 16px", borderRadius: "8px" }}>
                        <strong style={{ color: "#991b1b", display: "flex", alignItems: "center", gap: "6px" }}>
                          🚫 Missing Mandatory Skills
                        </strong>
                        <ul style={{ margin: "8px 0 0 0", paddingLeft: "20px", color: "#991b1b" }}>
                          {evalData.missing_mandatory_requirements.map((skill, i) => (
                            <li key={i}>{skill}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Render Missing Preferred Requirements */}
                    {evalData.missing_preferred_requirements?.length > 0 && (
                      <div style={{ backgroundColor: "#fff7ed", border: "1px solid #ffedd5", padding: "12px 16px", borderRadius: "8px" }}>
                        <strong style={{ color: "#c2410c", display: "flex", alignItems: "center", gap: "6px" }}>
                          ⚠️ Missing Preferred Skills
                        </strong>
                        <ul style={{ margin: "8px 0 0 0", paddingLeft: "20px", color: "#c2410c" }}>
                          {evalData.missing_preferred_requirements.map((skill, i) => (
                            <li key={i}>{skill}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                    {/* Render Strengths */}
                    {evalData.strengths?.length > 0 && (
                      <div style={{ backgroundColor: "#f0fdf4", border: "1px solid #bbf7d0", padding: "12px 16px", borderRadius: "8px" }}>
                        <strong style={{ color: "#166534", display: "flex", alignItems: "center", gap: "6px" }}>
                          ✅ Key Strengths
                        </strong>
                        <ul style={{ margin: "8px 0 0 0", paddingLeft: "20px", color: "#166534" }}>
                          {evalData.strengths.map((strength, i) => (
                            <li key={i}>{strength}</li>
                          ))}
                        </ul>
                      </div>
                    )}

                  </div>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default ResultsTable;