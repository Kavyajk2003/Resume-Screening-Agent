<p align="center">
  <h1>Resume Screening Agent</h1>
</p>

>  Revolutionize your hiring process by automating resume screening with AI-powered precision, identifying top talent faster and fairer.

## The Strategic "Why"

>  Hiring managers and recruiters face an overwhelming challenge: sifting through hundreds, often thousands, of resumes for a single role. This manual process is not only time-consuming and costly but is also prone to human bias, inconsistency, and the potential to overlook highly qualified candidates. The traditional approach stifles efficiency and hinders an organization's ability to swiftly secure top-tier talent.

This **Resume-Screening-Agent** provides a cutting-edge solution by automating and optimizing the initial stages of the hiring funnel. Leveraging advanced AI and machine learning, it intelligently parses, analyzes, and ranks resumes against specific job requirements. This empowers organizations to drastically reduce time-to-hire, enhance screening accuracy, mitigate unconscious bias, and focus human expertise on evaluating the most promising candidates, ultimately leading to superior hiring outcomes.

---

## Key Features

✨ **Intelligent Keyword Matching**: Automatically identifies and highlights relevant skills, experience, and qualifications based on job descriptions, ensuring no critical detail is missed.

🚀 **AI-Powered Candidate Ranking**: Ranks applicants by their suitability, providing a clear, data-driven hierarchy of top candidates, accelerating shortlisting.

🛡️ **Bias Mitigation Algorithms**: Designed to reduce unconscious bias by focusing on objective criteria, promoting a more diverse and equitable hiring process.

⚙️ **Customizable Screening Criteria**: Allows users to define and adjust specific parameters and weightings for roles, ensuring the agent aligns perfectly with unique hiring needs.

📊 **Comprehensive Resume Parsing**: Extracts structured data from various resume formats, transforming unstructured text into actionable insights.

🔗 **Scalable & Modular Architecture**: Built with a clear separation of concerns, enabling easy integration with existing HR systems and future expansion.

---

## Technical Architecture

This project is engineered with a robust, full-stack architecture, leveraging Python for powerful backend processing and JavaScript for a dynamic, responsive frontend.

### Tech Stack Overview

| Technology   | Purpose                                     | Key Benefit                                               |
| :----------- | :------------------------------------------ | :-------------------------------------------------------- |
| **Python**   | Backend logic, API, data processing, ML/AI  | Robust, scalable, extensive libraries for NLP & ML        |
| **JavaScript** | Frontend user interface, interactivity      | Dynamic, responsive, modern web experiences               |
| **Node.js**  | JavaScript runtime environment              | Enables server-side JS for tooling, build processes       |
| **`pip`/`venv`** | Python package management & isolation     | Clean dependencies, reproducible development environments |
| **(Web Framework)** | Backend API development (e.g., Flask/FastAPI) | Rapid development, structured API endpoints               |
| **(UI Framework)** | Frontend component-based UI (e.g., React/Vue) | Efficient rendering, reusable components                  |

### Directory Structure

```
Resume-Screening-Agent/
├── .gitignore
├── backend/
│   ├── app.py              # Main application entry point (e.g., Flask/FastAPI)
│   ├── services/           # Core business logic, screening algorithms
│   │   └── screening.py
│   ├── models/             # Data models for resume parsing, job descriptions
│   │   └── __init__.py
│   └── utils/              # Helper functions (e.g., file parsers, data transformers)
│       └── parser.py
├── frontend/
│   ├── public/             # Static assets (index.html, favicon, images)
│   │   └── index.html
│   ├── src/                # Frontend source code (e.g., React/Vue components)
│   │   ├── App.js          # Main application component
│   │   ├── components/     # Reusable UI components
│   │   └── index.js        # Frontend entry point
│   └── package.json        # Frontend JavaScript dependencies and scripts
└── requirements.txt        # Python dependencies for the backend environment
```

---

## Operational Setup

Follow these steps to get the Resume-Screening-Agent up and running on your local machine.

### Prerequisites

Ensure you have the following installed:

*   **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
*   **Node.js & npm (or Yarn)**: [Download Node.js](https://nodejs.org/en/download/) (npm is included; Yarn can be installed separately)

### Installation

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/Kavyajk2003/Resume-Screening-Agent
    cd Resume-Screening-Agent
    ```

2.  **Backend Setup (Python)**:
    *   Create and activate a Python virtual environment:
        ```bash
        python -m venv .venv
        # On macOS/Linux:
        source .venv/bin/activate
        # On Windows:
        .\venv\Scripts\activate
        ```
    *   Install the required Python packages:
        ```bash
        pip install --upgrade pip
        pip install -r requirements.txt
        ```
    *   Navigate into the backend directory:
        ```bash
        cd backend
        ```
    *   Start the backend server (example command, may vary based on framework):
        ```bash
        uvicorn backend.main:app --reload
        ```
    *   The backend API should now be running, typically on `http://localhost:8000` or similar.

3.  **Frontend Setup (JavaScript)**:
    *   Open a **new terminal window** and navigate to the project root, then into the frontend directory:
        ```bash
        cd Resume-Screening-Agent/frontend
        ```
    *   Install the frontend dependencies:
        ```bash
        npm install
        # Or if you prefer Yarn:
        # yarn install
        ```
    *   Start the frontend development server:
        ```bash
        npm start
        # Or if you prefer Yarn:
        # yarn start
        ```
    *   The frontend application should now be accessible in your web browser, typically at `http://localhost:3000`.

### Environment Configuration
This project may require specific environment variables for database connections, API keys, or other sensitive configurations.

1.  Create a `.env` file in the `backend` directory (and potentially `frontend` if client-side environment variables are needed) based on the example below:
    ```
    # frontend/.env (Example - for React apps, usually REACT_APP_ prefix)
    REACT_APP_API_BASE_URL="http://localhost:5000/api"
    # Add other frontend-specific variables here
    ```
2.  Populate these files with your specific values. **Do not commit `.env` files to version control.** `.gitignore` should already prevent this.

---

## Design Trade offs

### 1. Free AI service vs self-hosted LLM

I used Groq's free API because it provides very fast inference and doesn't require GPU infrastructure.

My laptop does not support good models
The tradeoff is dependency on an external API and rate limits.

### 2. Real-time processing vs background jobs

Resume screening happens synchronously after the upload.
For a small number of resumes this provides immediate feedback, but for hundreds of resumes a background queue would be more appropriate.

### 3. Prompt engineering vs complex business logic

Instead of writing many backend rules, I delegated decision-making to the LLM through carefully designed prompts.
This makes the backend simpler and easier to maintain while allowing business rules to evolve by updating prompts.

### 4. Build the application as Command line tool vs full stack web application

Initially, I considered a command-line approach where the recruiter would run terminal commands, provide the job description, and pass resume files as input. This approach is simpler to implement.
However, I chose a full-stack architecture using React for the frontend and FastAPI for the backend because it provides a much better user experience, play with the live application deployed and have a edge over other candidates.

## Limitations of this project
1. External AI dependency - The recommendation generation depends on Groq's API. If the service is unavailable or rate-limited, recommendations cannot be generated.

2. Limited document support - The parser currently focuses on common resume formats such as PDF, txt and DOCX. More complex layouts or scanned resumes may require OCR support.

3. Prompt-based reasoning - The final hiring recommendation depends on prompt engineering. While effective, prompt outputs can vary and are not as deterministic as rule-based systems.

4. Small-scale processing - Resumes are processed synchronously. For enterprise-scale screening of hundreds or thousands of resumes, asynchronous processing with a task queue would improve scalability.

5. Basic ATS logic - The system doesn't yet include configurable hiring rules, recruiter feedback loops, or historical hiring data.

## Community & Governance

We welcome contributions from the community to enhance and expand the capabilities of the Resume-Screening-Agent.

### Contributing

We adhere to a standard GitHub workflow for contributions:

1.  **Fork** the repository to your own GitHub account.
2.  **Clone** your forked repository to your local machine.
3.  **Create a new branch** for your feature or bug fix:
    ```bash
    git checkout -b feature/your-feature-name
    # Or for a bug fix:
    # git checkout -b bugfix/issue-description
    ```
4.  **Implement** your changes, ensuring adherence to coding standards and best practices.
5.  **Test** your changes thoroughly.
6.  **Commit** your changes with a clear and descriptive message.
7.  **Push** your branch to your forked repository.
8.  **Open a Pull Request** from your branch to the `main` branch of the original `Resume-Screening-Agent` repository. Provide a detailed description of your changes and their purpose.

We appreciate your efforts in improving this project!
