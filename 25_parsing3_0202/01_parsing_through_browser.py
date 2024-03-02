from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'https://selectel.ru/blog/'
driver.get(url)
share_btn = driver.find_element(By.CLASS_NAME, 'greetings_typed')
share_btn.click()

search = driver.find_element(By.XPATH, '//*[@id="search-modal"]/div/div[1]/div/div[1]/input')
search.send_keys('Git')
time.sleep(10)
