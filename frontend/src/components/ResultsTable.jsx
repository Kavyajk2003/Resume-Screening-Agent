function ResultsTable({ results }) {
  if (!results || results.length === 0) {
    return null;
  }

  return (
    <div style={{ marginTop: "30px" }}>
      <h2>Screening Results</h2>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "15px",
        }}
      >
        <thead>
          <tr style={{ backgroundColor: "#2563eb", color: "white" }}>
            <th style={styles.th}>Rank</th>
            <th style={styles.th}>Candidate</th>
            <th style={styles.th}>Score</th>
            <th style={styles.th}>Recommendation</th>
          </tr>
        </thead>

        <tbody>
          {results.map((candidate, index) => (
            <tr key={index}>
              <td style={styles.td}>{candidate.rank}</td>
              <td style={styles.td}>{candidate.candidate}</td>

              <td style={styles.td}>
                {Number(candidate.score).toFixed(2)}%
              </td>

              <td style={styles.td}>
                <pre
                  style={{
                    whiteSpace: "pre-wrap",
                    margin: 0,
                    fontFamily: "inherit",
                  }}
                >
                  {candidate.recommendation}
                </pre>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

const styles = {
  th: {
    padding: "12px",
    border: "1px solid #ddd",
  },

  td: {
    padding: "12px",
    border: "1px solid #ddd",
    verticalAlign: "top",
  },
};

export default ResultsTable;