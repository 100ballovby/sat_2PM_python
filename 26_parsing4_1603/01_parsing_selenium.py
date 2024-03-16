from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = 'https://dominos.by/ru/minsk/#Pizza'
driver.get(url)

pizza_wrapper = driver.find_element(By.CLASS_NAME, 'group-item__grid')
pizzas = pizza_wrapper.find_elements(By.CLASS_NAME, 'group-item__item')
with open('dominos.txt', 'w') as file:
	for pizza in pizzas:
		name = pizza.find_element(By.CLASS_NAME, 'group-item__name-product').text
		weight = pizza.find_element(By.CLASS_NAME, 'sizes-weight').text
		price = pizza.find_element(By.CLASS_NAME, 'group-item__price-text').text
		file.write(f'{name} вес: {weight}, Цена: {price}\n')

