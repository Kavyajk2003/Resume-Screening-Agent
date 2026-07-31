import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import ResultsTable from "./ResultsTable";

describe("ResultsTable Component", () => {
  const shortlistResults = [
    {
      candidate: "Kavya_Resume.pdf",
      score: 87.5,
      recommendation: {
        final_decision: "Shortlist",
        recommendation_summary:
          "Strong Java Full Stack profile with relevant experience.",
        evaluation: {
          missing_mandatory_requirements: [],
          missing_preferred_requirements: ["Docker"],
          strengths: [
            "Java",
            "Spring Boot",
            "React",
            "REST APIs",
          ],
        },
      },
    },
  ];

  const rejectResults = [
    {
      candidate: "Rahul_Resume.pdf",
      score: 0,
      recommendation: {
        final_decision: "Reject",
        recommendation_summary:
          "Candidate is missing mandatory skills.",
        evaluation: {
          missing_mandatory_requirements: [
            "Java",
            "Spring Boot",
          ],
          missing_preferred_requirements: [],
          strengths: [],
        },
      },
    },
  ];

  test("renders table headers", () => {
    render(<ResultsTable results={shortlistResults} />);

    expect(screen.getByText("Candidate File")).toBeInTheDocument();
    expect(screen.getByText("Match Score")).toBeInTheDocument();
    expect(screen.getByText("Decision")).toBeInTheDocument();
    expect(screen.getByText("Summary & Feedback")).toBeInTheDocument();
  });

  test("renders candidate filename", () => {
    render(<ResultsTable results={shortlistResults} />);

    expect(
      screen.getByText("Kavya_Resume.pdf")
    ).toBeInTheDocument();
  });

  test("renders semantic match score", () => {
    render(<ResultsTable results={shortlistResults} />);

    expect(
      screen.getByText("87.5%")
    ).toBeInTheDocument();
  });

  test("renders final decision badge", () => {
    render(<ResultsTable results={shortlistResults} />);

    expect(
      screen.getByText("Shortlist")
    ).toBeInTheDocument();
  });

  test("renders recommendation summary", () => {
    render(<ResultsTable results={shortlistResults} />);

    expect(
      screen.getByText(
        /Strong Java Full Stack profile/i
      )
    ).toBeInTheDocument();
  });

  test("renders strengths", () => {
    render(<ResultsTable results={shortlistResults} />);

    expect(screen.getByText("Java")).toBeInTheDocument();
    expect(screen.getByText("Spring Boot")).toBeInTheDocument();
    expect(screen.getByText("React")).toBeInTheDocument();
    expect(screen.getByText("REST APIs")).toBeInTheDocument();
  });

  test("renders missing preferred skills", () => {
    render(<ResultsTable results={shortlistResults} />);

    expect(screen.getByText("Docker")).toBeInTheDocument();

    expect(
      screen.getByText(/Missing Preferred Skills/i)
    ).toBeInTheDocument();
  });

  test("does not render mandatory skills section when there are no missing mandatory skills", () => {
    render(<ResultsTable results={shortlistResults} />);

    expect(
      screen.queryByText(/Missing Mandatory Skills/i)
    ).not.toBeInTheDocument();
  });

  test("renders reject decision", () => {
    render(<ResultsTable results={rejectResults} />);

    expect(
      screen.getByText("Reject")
    ).toBeInTheDocument();
  });

  test("renders missing mandatory skills", () => {
    render(<ResultsTable results={rejectResults} />);

    expect(
      screen.getAllByText(/Missing Mandatory Skills/i).length
    ).toBeGreaterThan(0);

    expect(
      screen.getByText("Java")
    ).toBeInTheDocument();

    expect(
      screen.getByText("Spring Boot")
    ).toBeInTheDocument();
  });

  test("renders recommendation summary for rejected candidate", () => {
    render(<ResultsTable results={rejectResults} />);

    expect(
      screen.getByText(
        /Candidate is missing mandatory skills/i
      )
    ).toBeInTheDocument();
  });

  test("renders headers even when no results are provided", () => {
    render(<ResultsTable results={[]} />);

    expect(
      screen.getByText("Candidate File")
    ).toBeInTheDocument();

    expect(
      screen.queryByText("Kavya_Resume.pdf")
    ).not.toBeInTheDocument();
  });
});