from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random


driver = webdriver.Firefox()

wait = WebDriverWait(driver, 3)

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys("Random")

dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "G43f7e")))

options = dropdown.find_elements(By.TAG_NAME, "li")

limited_options = options[:10]

random_option = random.choice(options)

print(random_option)

random_option.click()

driver.quit()