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

for pizza in pizzas:
	size_btn = pizza.find_element(By.CSS_SELECTOR, ".sizes-block .base-tab-button:nth-of-type(2)") # найти вторую кнопку в блоке с размерами
	red_btn = pizza.find_element(By.CLASS_NAME, 'red-button')
	try:
		size_btn.click()
		red_btn.click()
	except:
		pass

cart = driver.find_element(By.CLASS_NAME, 'header-cart__order-btn')
cart.click()
field_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first_name"]')
field_name.send_keys('Демид')
field_phone = driver.find_element(By.CSS_SELECTOR, 'input[name="phone_number"]')
field_phone.send_keys('375291234567')

street = driver.find_element(By.CSS_SELECTOR, '.checkout-form__address-block-street')
street_input = street.find_element(By.CLASS_NAME, 'rect-input__input')
street_input.send_keys('Красная ул.')
select = driver.find_elements(By.CSS_SELECTOR, 'rect-input__dropdown-list button')
for sel in select:
	print(sel.text)

house = driver.find_element(By.CSS_SELECTOR, 'input[name="street_number"]')
house.send_keys('7А')

pay = driver.find_element(By.CSS_SELECTOR, 'input[name="cash"]')
pay.click()

order = driver.find_element(By.CSS_SELECTOR, '.red-button')
order.click()

time.sleep(5)


