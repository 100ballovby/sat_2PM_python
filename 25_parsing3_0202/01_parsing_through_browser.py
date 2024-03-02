from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'https://selectel.ru/blog/'
driver.get(url)  # подключаюсь к странице браузером
share_btn = driver.find_element(By.CLASS_NAME, 'greetings_typed')  # нахожу кнопку для поиска
share_btn.click()  # нажимаю кнопку для поиска по сайту

search = driver.find_element(By.XPATH, '//*[@id="search-modal"]/div/div[1]/div/div[1]/input')
# ^ нахожу поле для ввода на странице
search.send_keys('Демид Раксин')  # записываю в это поле текст
time.sleep(10)
