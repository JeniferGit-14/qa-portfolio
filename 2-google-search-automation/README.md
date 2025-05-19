
---

### 📁 `2_Google_Search_Automation/README.md`

```markdown
# 🔍 Google Search Automation

## ✅ Objective
Automate a basic Google search and verify the result page title.

## 🛠️ Tools Used
- Selenium
- Python
- ChromeDriver

## 📋 What I Did
- Opened Google.com
- Searched for "OpenAI"
- Verified the page title includes the search keyword

## 🧪 Sample Code
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("OpenAI")
search_box.send_keys(Keys.RETURN)

assert "OpenAI" in driver.title
driver.quit()
