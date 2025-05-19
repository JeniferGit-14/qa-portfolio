
---

### 📁 `3_Form_File_Upload_Automation/README.md`

```markdown
# 📄 Form Automation with File Upload

## ✅ Objective
Automate filling out a sample form including a file upload and success message verification.

## 🛠️ Tools Used
- Selenium
- Python
- ChromeDriver

## 📋 What I Did
- Visited a sample form page
- Filled out fields (name, email, etc.)
- Uploaded a `.txt` file
- Submitted the form and verified the success message

## 🧪 Sample Code
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/sample-qa-form/")

driver.find_element(By.NAME, "g1103-name").send_keys("Jeni QA")
driver.find_element(By.NAME, "g1103-email").send_keys("jeni@example.com")
driver.find_element(By.NAME, "file-553").send_keys(r"C:\Users\jenif\OneDrive\Desktop\Jeni A.txt")

driver.find_element(By.ID, "gform_submit_button_1103").click()
time.sleep(3)

assert "Thanks for contacting us" in driver.page_source
driver.quit()
