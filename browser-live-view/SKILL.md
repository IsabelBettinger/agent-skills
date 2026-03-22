---
name: browser-live-view
description: Real-time browser automation with live visibility into browser state, DOM inspection, console logs, network activity, and screenshot capture. Use when user wants you to see their browser in real-time without manual screenshots, debug web applications, automate browser workflows, or interact with web pages autonomously.
---

# Browser Live View Skill

This skill provides comprehensive real-time browser automation using Playwright with live visibility into browser state, DOM inspection, console logs, network activity, and autonomous interaction capabilities.

---

## Overview

Browser Live View enables AI agents to see and interact with web browsers in real-time without requiring users to manually take screenshots or perform actions. The agent can:
- **See** what's happening in the browser (screenshots, DOM state)
- **Interact** with web pages (click, type, navigate)
- **Debug** issues (console logs, network activity)
- **Automate** workflows (fill forms, scrape data, test flows)

---

## When to Use This Skill

**Trigger When:**
- User asks you to "see my browser" or "look at what's happening"
- User wants you to debug a web application issue
- User needs help filling out forms or interacting with web pages
- User wants you to automate browser workflows
- User is testing a web application and wants you to verify functionality
- User needs screen capture or screenshot analysis
- User wants real-time monitoring of web page behavior

**Do Not Trigger When:**
- Simple code questions unrelated to browser interaction
- File operations that don't involve web browsers
- General programming tasks without browser component

---

## Top Capabilities

### 1. Live Browser State Inspection
**See what's happening in the browser:**
- Take screenshots of current page state
- Inspect DOM elements and their properties
- View page title, URL, and metadata
- Monitor element visibility and positioning
- Track JavaScript variable states

### 2. Autonomous Browser Interaction
**Control the browser like a user would:**
- Click on elements (buttons, links, dropdowns)
- Type text into input fields
- Select options from dropdowns/checkboxes
- Navigate between pages (click links, submit forms)
- Scroll and interact with dynamic content
- Handle alerts, dialogs, and popups

### 3. Console & Debugging
**Debug JavaScript and web applications:**
- Capture console logs (all levels: log, warn, error)
- Monitor network requests and responses
- Track failed network calls
- View response bodies and headers
- Measure page performance metrics

### 4. Screenshot & Visual Capture
**Document browser state:**
- Full-page screenshots
- Element-specific screenshots
- Before/after comparisons
- Error state capture
- Video recording of interactions (optional)

### 5. Web Scraping & Data Extraction
**Extract data from web pages:**
- Pull text content from elements
- Extract table data
- Capture form data
- Scrape structured data (JSON, CSV)
- Monitor dynamic content changes

### 6. Form Automation
**Fill and submit forms:**
- Auto-fill form fields
- Handle validation and error states
- Upload files
- Submit forms and capture responses
- Multi-step form workflows

---

## Setup & Configuration

### Prerequisites

**Install Playwright:**
```bash
# Install via npm
npm install playwright

# Install browser binaries
npx playwright install chromium
npx playwright install firefox
npx playwright install webkit
```

**Python Installation:**
```bash
# Install Python package
pip install playwright

# Install browsers
playwright install
```

### Launch Browser for AI Agent Control

**For Claude Desktop or OpenCode:**

Create a dedicated browser profile:
```bash
# Create a new browser profile directory
mkdir -p ~/browser-for-ai

# Launch browser with remote debugging enabled
google-chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=~/browser-for-ai \
  --new-window \
  https://example.com
```

Or use Playwright to launch controlled browser:
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=False,  # Show browser window
        args=['--start-maximized']
    )
    page = browser.new_page()
    # Agent can now see and control browser
```

---

## Best Practices

### DO:

1. **Take screenshots before and after interactions** to verify changes
2. **Check console logs** to catch JavaScript errors early
3. **Wait for elements** to be visible/clickable before interacting
4. **Use explicit waits** instead of hard-coded delays
5. **Handle errors gracefully** with try/catch blocks
6. **Document the workflow** step-by-step for complex automations
7. **Test selectors** before relying on them (elements may change)
8. **Respect rate limits** - don't overwhelm servers with rapid requests
9. **Use headless mode** for background tasks, visual mode for debugging
10. **Monitor network activity** to understand API calls and data flow

### DON'T:

1. **Don't assume elements are clickable** - always wait for them
2. **Don't ignore console errors** - they often reveal the root cause
3. **Don't hard-code sleep delays** - use explicit waits instead
4. **Don't click without verification** - check element state first
5. **Don't ignore rate limits** - respect server capacity
6. **Don't scrape without permission** - check robots.txt and ToS
7. **Don't leave browsers open** - always close when done
8. **Don't trust page structure** - verify selectors before use
9. **Don't skip error handling** - expect things to break
10. **Don't forget to document** - future you will thank you

---

## Common Use Cases

### 1. Web Application Debugging

**Scenario:** User reports a bug on a web app

**Agent Workflow:**
1. Navigate to the problematic page
2. Take screenshot of current state
3. Check console for errors
4. Interact to reproduce the issue
5. Take screenshot of error state
6. Analyze and identify root cause
7. Report findings to user

**Example Commands:**
```python
# Navigate to page
page.goto("https://example.com/problematic-page")

# Take screenshot
page.screenshot(path="before_interaction.png")

# Check for console errors
console_messages = []
page.on("console", lambda msg: console_messages.append(msg.text))
page.on("pageerror", lambda exc: console_messages.append(str(exc)))

# Reproduce the bug
page.click("#submit-button")
page.wait_for_timeout(1000)

# Document error state
page.screenshot(path="error_state.png")
print("Console errors:", console_messages)
```

### 2. Form Filling & Automation

**Scenario:** User needs help filling out a complex form

**Agent Workflow:**
1. Navigate to form page
2. Analyze form structure
3. Fill fields one by one
4. Handle validation errors
5. Submit form
6. Capture confirmation/success page

**Example Commands:**
```python
# Navigate to form
page.goto("https://example.com/form")

# Fill form fields
page.fill("#name", "John Doe")
page.fill("#email", "john@example.com")
page.select_option("#country", "US")
page.check("#terms-checkbox")

# Handle validation if needed
page.click("#submit")
page.wait_for_selector(".error-message", state="visible", timeout=5000)

# Fix any errors
error_text = page.text_content(".error-message")
print(f"Validation error: {error_text}")

# Submit again
page.fill("#phone", "+1-555-0100")
page.click("#submit")
page.wait_for_url("**/success**")

# Capture success
page.screenshot(path="form_success.png")
```

### 3. Data Scraping

**Scenario:** User needs to extract data from a web page

**Agent Workflow:**
1. Navigate to data page
2. Wait for data to load
3. Extract structured data
4. Handle pagination if needed
5. Save data to file

**Example Commands:**
```python
# Navigate to page
page.goto("https://example.com/data-table")

# Wait for data to load
page.wait_for_selector("table.data tbody tr")

# Extract table data
rows = page.query_selector_all("table.data tbody tr")
data = []
for row in rows:
    cols = row.query_selector_all("td")
    data.append({
        "name": cols[0].text_content(),
        "value": cols[1].text_content(),
        "date": cols[2].text_content()
    })

# Save to file
import json
with open("scraped_data.json", "w") as f:
    json.dump(data, f, indent=2)

# Take screenshot of data
page.screenshot(path="scraped_data.png")
```

### 4. E-commerce Workflow Testing

**Scenario:** User wants to test a checkout flow

**Agent Workflow:**
1. Navigate to product page
2. Add item to cart
3. Proceed to checkout
4. Fill shipping info
5. Complete payment (test mode)
6. Verify success

**Example Commands:**
```python
# Start checkout flow
page.goto("https://shop.example.com/product/123")
page.click(".add-to-cart")
page.wait_for_selector(".cart-badge")
page.click(".view-cart")

# Proceed through checkout
page.click(".checkout-button")
page.fill("#shipping-name", "Test User")
page.fill("#shipping-address", "123 Test St")
page.fill("#shipping-city", "Test City")
page.select_option("#shipping-state", "CA")
page.fill("#shipping-zip", "90210")

# Continue to payment
page.click(".continue-to-payment")
page.wait_for_selector("#card-number")

# Fill payment (test card)
page.fill("#card-number", "4242424242424242")
page.fill("#card-expiry", "12/25")
page.fill("#card-cvc", "123")

# Complete order
page.click(".place-order")
page.wait_for_selector(".order-confirmation")

# Document success
order_number = page.text_content(".order-number")
page.screenshot(path="order_success.png")
print(f"Order confirmed: {order_number}")
```

### 5. Real-time Page Monitoring

**Scenario:** User wants to monitor a page for changes

**Agent Workflow:**
1. Navigate to page
2. Capture initial state
3. Monitor for changes over time
4. Alert on specific conditions
5. Document findings

**Example Commands:**
```python
# Navigate and capture initial state
page.goto("https://example.com/dashboard")
initial_html = page.content()
initial_screenshot = page.screenshot()

# Monitor for 60 seconds, checking every 5 seconds
for i in range(12):
    page.wait_for_timeout(5000)
    
    # Check for specific condition
    status = page.text_content(".status-indicator")
    if status != "Ready":
        print(f"Alert: Status changed to {status}")
        page.screenshot(path=f"alert_{i}.png")
    
    # Check for new content
    current_html = page.content()
    if current_html != initial_html:
        print("Page content changed!")
        page.screenshot(path=f"change_{i}.png")
        initial_html = current_html

# Final screenshot
page.screenshot(path="final_state.png")
```

---

## Advanced Features

### Network Interception

**Monitor and modify network requests:**
```python
# Track all network requests
requests = []
page.on("request", lambda req: requests.append({
    "url": req.url,
    "method": req.method,
    "headers": req.headers
}))

# Track responses
responses = []
page.on("response", lambda res: responses.append({
    "url": res.url,
    "status": res.status,
    "body": res.text()
}))

# Navigate
page.goto("https://example.com/api-page")

# Analyze network activity
for req, res in zip(requests, responses):
    if res["status"] >= 400:
        print(f"Failed request: {req['url']} - {res['status']}")
```

### File Upload

**Handle file uploads:**
```python
# Set up file chooser handler
with page.expect_file_chooser() as fc_info:
    page.click("#upload-button")

file_chooser = fc_info.value
file_chooser.set_files("/path/to/file.pdf")

# Wait for upload to complete
page.wait_for_selector(".upload-success")
```

### Drag and Drop

**Perform drag and drop operations:**
```python
# Drag element from source to target
source = page.query_selector(".draggable")
target = page.query_selector(".dropzone")

source.drag_to(target)
page.wait_for_selector(".dropzone.filled")
```

### Keyboard Shortcuts

**Execute keyboard shortcuts:**
```python
# Type with keyboard shortcuts
page.keyboard.press("Control+a")
page.keyboard.press("Control+c")

# Type and submit
page.keyboard.type("Search query")
page.keyboard.press("Enter")
```

### Multiple Pages/Tabs

**Handle multiple browser tabs:**
```python
# Open new tab
page1 = browser.contexts[0].pages[0]
page2 = browser.contexts[0].new_page()

# Switch between tabs
page2.goto("https://example.com/page2")
page1.screenshot(path="page1.png")
page2.screenshot(path="page2.png")
```

### Authentication & Cookies

**Handle login and sessions:**
```python
# Navigate to login
page.goto("https://example.com/login")

# Fill credentials
page.fill("#username", "user@example.com")
page.fill("#password", "password123")
page.click(".login-button")

# Wait for redirect
page.wait_for_url("**/dashboard**")

# Save cookies for reuse
cookies = page.context.cookies()
with open("session_cookies.json", "w") as f:
    json.dump(cookies, f)

# In future session, load cookies
with open("session_cookies.json", "r") as f:
    cookies = json.load(f)
page.context.add_cookies(cookies)
```

---

## Error Handling

### Common Errors and Solutions

**1. Element Not Found**
```python
# Don't do this
page.click("#missing-button")  # May fail

# Do this instead
page.wait_for_selector("#missing-button", timeout=10000)
page.click("#missing-button")
```

**2. Stale Element Reference**
```python
# After page navigation, re-query elements
page.goto("https://example.com")
button = page.query_selector("#action-button")
page.click("#other-button")  # Page updates
# Don't use 'button' variable - requery it
page.click("#action-button")  # Re-query
```

**3. Timeout Errors**
```python
# Increase timeout for slow pages
page.wait_for_selector(".dynamic-content", timeout=30000)

# Or wait for specific condition
page.wait_for_function("document.querySelector('.status').textContent === 'Ready'")
```

**4. Popup/Alert Handling**
```python
# Handle alert dialogs
page.on("dialog", lambda dialog: dialog.accept())
page.click(".dangerous-action")  # Will trigger confirmation
```

**5. Iframe Access**
```python
# Switch to iframe
frame = page.frame(name="iframe-name")
frame.fill("#input-in-iframe", "value")

# Or by selector
frame = page.frame_locator("iframe[name='content']")
frame.fill("#input", "value")
```

---

## Performance & Optimization

### Speed Up Browser Automation

1. **Use headless mode** for background tasks:
   ```python
   browser = p.chromium.launch(headless=True)
   ```

2. **Disable images** for faster page loads:
   ```python
   context = browser.new_context(
       extra_http_headers={"Accept-Language": "en-US"}
   )
   # Block images in page route
   page.route("**/*.{png,jpg,jpeg,gif}", lambda route: route.abort())
   ```

3. **Use locators instead of page methods:**
   ```python
   # Slower
   page.click("#button")
   
   # Faster
   page.locator("#button").click()
   ```

4. **Parallel execution** when possible:
   ```python
   browser = p.chromium.launch()
   context = browser.new_context()
   
   # Create multiple pages
   page1 = context.new_page()
   page2 = context.new_page()
   
   # Navigate in parallel
   page1.goto("https://example.com/page1")
   page2.goto("https://example.com/page2")
   ```

5. **Reuse browser context:**
   ```python
   # Don't launch new browser for each task
   # Reuse same browser with multiple pages
   ```

---

## Security Considerations

### Do:
- ✅ Verify URLs before navigating (prevent SSRF)
- ✅ Handle sensitive data carefully (passwords, tokens)
- ✅ Use HTTPS whenever possible
- ✅ Respect robots.txt and website terms
- ✅ Implement rate limiting
- ✅ Validate and sanitize scraped data
- ✅ Use test environments for automation

### Don't:
- ❌ Store credentials in plain text
- ❌ Navigate to untrusted URLs blindly
- ❌ Scrape protected/copyrighted content
- ❌ Ignore website terms of service
- ❌ Perform automated attacks or abuse
- ❌ Leave browser sessions open unattended
- ❌ Expose internal systems via browser automation

---

## Tools & Dependencies

### Python (Recommended)
```bash
pip install playwright
playwright install
```

### Node.js
```bash
npm install playwright
npx playwright install
```

### Java
```bash
# Maven
<dependency>
    <groupId>com.microsoft.playwright</groupId>
    <artifactId>playwright</artifactId>
    <version>1.40.0</version>
</dependency>
```

### Additional Tools
- **Screenshot comparison:** Use `playwright-visual-regression` for visual diffs
- **Video recording:** `ffmpeg` for recording browser interactions
- **Mobile testing:** Device emulation available in Playwright

---

## Quick Reference Commands

### Navigation
```python
page.goto("https://example.com")
page.go_back()
page.go_forward()
page.reload()
```

### Finding Elements
```python
page.query_selector("#id")           # First match
page.query_selector_all(".class")    # All matches
page.locator("button").first
page.locator("button").last
```

### Interactions
```python
page.click("#button")
page.dblclick("#element")
page.right_click("#element")
page.fill("#input", "text")
page.select_option("#dropdown", "value")
page.check("#checkbox")
page.uncheck("#checkbox")
```

### Assertions
```python
page.assert_title("Expected Title")
page.assert_url("**/expected-path**")
page.assert_selector_visible("#element")
page.assert_text_content("#element", "Expected Text")
```

### Screenshot
```python
page.screenshot()  # Viewport only
page.screenshot(full_page=True)  # Full page
page.screenshot(path="screenshot.png")
```

---

## Example: Complete Workflow

```python
from playwright.sync_api import sync_playwright
import json

def automate_workflow(url):
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        try:
            # Navigate
            page.goto(url)
            
            # Set up monitoring
            console_logs = []
            errors = []
            page.on("console", lambda msg: console_logs.append(msg.text))
            page.on("pageerror", lambda exc: errors.append(str(exc)))
            
            # Take initial screenshot
            page.screenshot(path="step1_initial.png")
            
            # Interact
            page.click("#action-button")
            page.wait_for_selector(".result", timeout=10000)
            
            # Document result
            page.screenshot(path="step2_result.png")
            result_text = page.text_content(".result")
            
            # Report findings
            print(f"Result: {result_text}")
            print(f"Console logs: {console_logs}")
            if errors:
                print(f"Errors: {errors}")
            
            return {
                "success": True,
                "result": result_text,
                "screenshots": ["step1_initial.png", "step2_result.png"]
            }
            
        except Exception as e:
            page.screenshot(path="error_state.png")
            print(f"Error: {str(e)}")
            return {"success": False, "error": str(e)}
            
        finally:
            browser.close()

# Run workflow
result = automate_workflow("https://example.com")
print(json.dumps(result, indent=2))
```

---

## Notes for AI Agents

- **Always take screenshots** before and after interactions to maintain visibility
- **Check console logs** - they're often more informative than visual errors
- **Wait for elements** explicitly rather than using sleep/delay
- **Handle errors gracefully** - browsers can be unpredictable
- **Document everything** - future debugging will be easier
- **Respect rate limits** - don't overwhelm servers
- **Test selectors** - web pages change, verify before relying on them
- **Use appropriate timeouts** - slow pages need longer waits
- **Close browsers when done** - prevent resource leaks
- **Monitor network activity** - understand what's happening under the hood
