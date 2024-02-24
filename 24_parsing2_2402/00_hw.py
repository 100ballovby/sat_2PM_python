from bs4 import BeautifulSoup
import requests as req


url = 'https://dominos.by/ru/minsk/#Pizza'
page = req.get(url)


print(page.content)



