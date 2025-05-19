from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the Chrome driver
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the practice form
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

# Wait for 5 seconds so the page can load fully
time.sleep(5)

# Fill in the First Name
driver.find_element(By.NAME, "firstname").send_keys("John")

# Fill in the Last Name
driver.find_element(By.NAME, "lastname").send_keys("Doe")

# Select Gender (Male)
driver.find_element(By.ID, "sex-0").click()

# Select Years of Experience (5)
driver.find_element(By.ID, "exp-4").click()

# Select Profession (Automation Tester)
driver.find_element(By.ID, "profession-1").click()

# Select Automation Tool (Selenium Webdriver)
driver.find_element(By.ID, "tool-2").click()

# Upload a file
upload_element = driver.find_element(By.ID, "photo")
upload_element.send_keys("C:\\Users\\jenif\\OneDrive\\Desktop\\Jeni A.txt")

# Wait before closing
time.sleep(5)

# Close the browser
driver.quit()
