import { render, screen, fireEvent } from "@testing-library/react";
import "@testing-library/jest-dom";
import JobDescription from "./JobDescription";

describe("JobDescription Component", () => {

  test("renders the Job Description heading", () => {
    render(
      <JobDescription
        jobDescription=""
        setJobDescription={() => { }}
      />
    );

    expect(
      screen.getByRole("heading", {
        name: /Job Description/i,
      })
    ).toBeInTheDocument();
  });

  test("renders the textarea", () => {
    render(
      <JobDescription
        jobDescription=""
        setJobDescription={() => { }}
      />
    );

    expect(
      screen.getByPlaceholderText(/Paste the Job Description here/i)
    ).toBeInTheDocument();
  });

  test("displays the passed job description", () => {
    render(
      <JobDescription
        jobDescription="Java Full Stack Developer"
        setJobDescription={() => { }}
      />
    );

    expect(
      screen.getByDisplayValue("Java Full Stack Developer")
    ).toBeInTheDocument();
  });

  test("calls setJobDescription when typing", () => {
    const mockSetJobDescription = vi.fn();

    render(
      <JobDescription
        jobDescription=""
        setJobDescription={mockSetJobDescription}
      />
    );

    const textarea = screen.getByPlaceholderText(
      /Paste the Job Description here/i
    );

    fireEvent.change(textarea, {
      target: {
        value: "Python Developer",
      },
    });

    expect(mockSetJobDescription).toHaveBeenCalledTimes(1);

    expect(mockSetJobDescription).toHaveBeenCalledWith(
      "Python Developer"
    );
  });

  test("textarea has 10 rows", () => {
    render(
      <JobDescription
        jobDescription=""
        setJobDescription={() => { }}
      />
    );

    const textarea = screen.getByPlaceholderText(
      /Paste the Job Description here/i
    );

    expect(textarea).toHaveAttribute("rows", "10");
  });

});