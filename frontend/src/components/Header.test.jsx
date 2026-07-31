import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import Header from "./Header";

describe("Header Component", () => {
  test("renders the main heading", () => {
    render(<Header />);

    const heading = screen.getByRole("heading", {
      name: /AI Resume Screening Agent/i,
    });

    expect(heading).toBeInTheDocument();
  });

  test("renders the subtitle", () => {
    render(<Header />);

    const subtitle = screen.getByText(
      /Smart Resume Ranking using AI/i
    );

    expect(subtitle).toBeInTheDocument();
  });

  test("renders a header element", () => {
    const { container } = render(<Header />);

    const header = container.querySelector("header");

    expect(header).toBeInTheDocument();
  });

  test("renders an h1 heading", () => {
    render(<Header />);

    const heading = screen.getByRole("heading", {
      level: 1,
    });

    expect(heading).toHaveTextContent(
      "AI Resume Screening Agent"
    );
  });
});