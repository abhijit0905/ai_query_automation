# MCP Automation with Playwright

This document explains how we use Microsoft’s Playwright (via the MCP protocol) to drive browser interactions for our AI Query Automation tool. The goal is to simulate human‐like browsing—clicking, typing, waiting for results—so that Groq handles intent, and Playwright handles the heavy lifting.

## 🧩 Architecture Overview

1. **Intent Parsing (Groq)**

   * Takes natural language queries and returns structured parameters (category, max\_price, or flight details).
2. **Browser Automation (Playwright MCP)**

   * Launches a headless or headed Chromium instance.
   * Navigates to the target site (Amazon, Flipkart, etc.).
   * Performs form fills, clicks, and scrolls to load dynamic content.
3. **Data Extraction**

   * Uses CSS selectors to grab titles, prices, and links.
   * Falls back to human‐readable element queries if sites update their layout.
4. **Excel Reporting**

   * Packages the extracted data into `output.xlsx` with clear columns and filters.

---

## ⚙️ Playwright Setup

1. **Install Playwright**:

   ```bash
   pip install playwright
   playwright install
   ```
2. **Launch a Browser**:

   ```python
   from playwright.sync_api import sync_playwright

   with sync_playwright() as p:
       browser = p.chromium.launch(headless=True)
       page = browser.new_page()
       page.goto("https://www.amazon.in/")
       # ... your automation steps here
       browser.close()
   ```

---

## 🤖 Sample Automation Steps for Amazon

```python
# Navigate to Amazon search page
page.goto(f"https://www.amazon.in/s?k={category}")

# Wait for listings to render
page.wait_for_selector("div.s-main-slot[data-component-type='s-search-result']", timeout=60000)

# Scroll to load more items
for _ in range(3):
    page.mouse.wheel(0, 2000)
    page.wait_for_timeout(1000)

# Extract product cards
cards = page.query_selector_all("div.s-main-slot div[data-component-type='s-search-result']")
for card in cards[:10]:
    # Extract title, price, link
    info = extract_product_info(card)
    results.append(info)
```

---

## 🛡️ Error Handling & Resilience

* **Timeouts**: Generous wait times (up to 60 s) to accommodate slow loads.
* **Popup Management**: Detect and close login/outdated pop-ups with `page.click()` inside try/except.
* **Layout Changes**: Fallback selectors and debug logs to identify when site structure shifts.

---

## 🚀 Putting It All Together

1. **User enters a query** → Groq returns structured parameters.
2. **Main script** picks the right scraper module (Amazon, Flipkart, or flights).
3. **Playwright** runs the MCP steps to get raw data.
4. **Product utilities** clean and format the data.
5. **Excel writer** generates the final report.

With this setup, our AI tool feels like a real user browsing the web—robust, adaptable, and fast.
