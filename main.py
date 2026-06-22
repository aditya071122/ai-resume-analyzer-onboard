from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Signup
    email = ""
    password = "123456"

    page.goto("https://ai-resume-analyzer-onboard.vercel.app/")
    page.click("a.submit-btn")

    page.fill("input[type='email']", email)
    page.fill("input[type='password']", password)

    page.click("button[type='submit']")

    # Login
    page.goto("https://ai-resume-analyzer-onboard.vercel.app/login")

    page.fill("input[type='email']", email)
    page.fill("input[type='password']", password)

    page.click("button[type='submit']")

    # Upload Resume
    page.set_input_files(
    "#file-input",
    "ADITYARESUME.pdf"
    )

    # Enter JD
    jd_text = """
    Looking for QA Automation Engineer.

    Skills Required:
    - Python
    - Playwright
    - API Testing
    - SQL
    """
    page.fill("input[type='text']", jd_text)

    # Submit Evaluation
    page.click("#analyze-btn")
    # Validate Response Appears
    page.wait_for_selector("#results-section", timeout=60000)

    assert page.locator("#results-section").is_visible()

    print("Response appeared successfully")


    browser.close()