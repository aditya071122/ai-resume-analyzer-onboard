# AI Resume Analyzer - Playwright Automation

## Overview

This project automates the end-to-end workflow of the AI Resume Analyzer web application using Playwright with Python.

The automation covers:

* User Signup
* User Login
* Resume Upload
* Job Description (JD) Submission
* Resume Analysis
* Response Validation

---

## Tech Stack

* Python 3.x
* Playwright
* Chromium Browser

---

## Project Structure

```
Playwright/
│
├── main.py
├── RESUME.pdf
├── requirements.txt
└── README.md
```

---

## Test Scenario Covered

### 1. Signup

* Navigate to application homepage
* Open Signup page
* Enter email
* Enter password
* Submit registration form

### 2. Login

* Navigate to Login page
* Enter valid credentials
* Submit login form

### 3. Resume Upload

* Upload a valid PDF resume

### 4. Job Description Entry

* Enter a sample QA Automation Engineer JD

### 5. Resume Evaluation

* Click Analyze button
* Wait for evaluation response

### 6. Validation

* Verify results section appears successfully
* Test passes if response is displayed

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd ai-resume-analyzer-onboard
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## requirements.txt

```txt
playwright==1.54.0

```

---

## Test Data

### Credentials

```python
email = "your_email@example.com"
password = "123456"
```

### Resume File

```text
RESUME.pdf
```

Place the resume file in the project root directory.

---

## Execute Test

Run directly:

```bash
python main.py
```



---

## Expected Result

After successful execution:

```text
Response appeared successfully
```

The test validates that:

* User can sign up
* User can log in
* Resume uploads successfully
* JD is submitted
* AI evaluation result is generated
* Results section becomes visible

---

## Future Enhancements

* Page Object Model (POM)
* Data-driven testing
* Screenshot capture on failure
* HTML reporting
* Parallel execution
* Cross-browser testing
* CI/CD integration with GitHub Actions

---

## Application Under Test

AI Resume Analyzer

URL:

https://ai-resume-analyzer-onboard.vercel.app/

---

## Author

Aditya Gupta

Software Test Engineer
