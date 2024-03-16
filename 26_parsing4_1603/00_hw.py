from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'https://google.com'
driver.get(url)  # подключаюсь к странице браузером
search_field = driver.find_element(By.CLASS_NAME, 'gLFyf')  # нахожу поле ввода поискового запроса
search_field.send_keys('как научиться программировать')  # записываю в это поле текст
search_field.submit()  # так как поиск в гугле - это форма, отправляем ее методом submit 

time.sleep(10)
