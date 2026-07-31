function Header() {
  return (
    <header style={styles.header}>
      <h1>AI Resume Screening Agent</h1>
      <p>Smart Resume Ranking using AI</p>
    </header>
  );
}

const styles = {
  header: {
    background: "#2563eb",
    color: "white",
    padding: "20px",
    borderRadius: "10px",
    textAlign: "center",
    marginBottom: "30px",
  },
};

export default Header;