from bs4 import BeautifulSoup
import requests as req
import openpyxl


def parse_7745(category):
    url = f"https://7745.by/catalog/{category}?limit=1000"
    page = req.get(url)

    allLaptops = []
    filteredLaptops = []

    soup = BeautifulSoup(page.text, "html.parser")  # превращаю страницу сайта в объект, с которым можно работать
    allLaptops = soup.findAll('div', class_='catalog-item__wrapper')  # находим все div с классом catalog-item__wrapper (карточки товаров)

    wb = openpyxl.Workbook()  # создаю новую таблицу Excel
    sheet = wb.active  # получаю главный лист таблицы
    sheet.title = category.capitalize()

    sheet.append(['Название товара', 'Стоимость', 'Артикул'])  # добавление заголовков таблицы
    for laptop in allLaptops:
        name = laptop.find('a', class_='item-block_name').text
        price = laptop.find('div', class_='item-block_main-price-block').find('span').text.strip()[:9]
        art = laptop.find('div', class_='product__actions-block--right').find('span').text.strip()
        row = [name, price, art]
        sheet.append(row)

    wb.save(f'7745_res_{category}.xlsx')

cat = ['noutbuki', 'smartfony', 'televizory']
for categ in cat:
    parse_7745(categ)

