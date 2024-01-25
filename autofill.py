from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Rest of the code...
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get(r"http://127.0.0.1:5500/selenium_autofill/index.html")
current_url = driver.current_url

email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "password")

email_field.send_keys("test@example.com")
password_field.send_keys("password123")

time.sleep(3)

login_button = driver.find_element(By.XPATH, "//input[@value='Login']")
login_button.submit()

time.sleep(3)

try:
    for request in driver.requests:
        response_body = request.response.body.find(b'{"message"')
        if response_body == 0:
            message = request.response.body.decode("utf-8")
            print(message)
except:
    print("No response found")

wait = WebDriverWait(driver, 10)
wait.until(EC.url_changes(current_url))

text_field = driver.find_element(By.ID, "text")

text_field.send_keys("This is a test message with at least 30 characters.")

time.sleep(3)

submit_button = driver.find_element(By.XPATH, "//input[@value='Submit']")
submit_button.submit()

time.sleep(3)

try:
    for request in driver.requests:
        response_body = request.response.body.find(b'{"message"')
        if response_body == 0:
            message = request.response.body.decode("utf-8")
            print(message)
except:
    print("No response found")

driver.quit()
