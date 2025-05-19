from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Go to Google
driver.get("https://www.google.com")

# Find the search box and type "OpenAI"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("OpenAI")
search_box.send_keys(Keys.RETURN)

# Wait for results to load
time.sleep(2)

# Print the title of the page
print("Page Title:", driver.title)

# Close the browser
driver.quit()
