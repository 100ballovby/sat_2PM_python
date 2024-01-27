import requests as req

url = 'https://api.imgflip.com/get_memes'
response = req.get(url)

memes = response.json()['data']['memes']
for meme in memes:
    image_url = meme['url']  # сохраняю ссылку на картинку
    image_name = meme['name'].replace(' ', '_') + '.jpg'  # Drake_Hotline_Bling.jpg
    with open(image_name, 'wb') as file:
        resp = req.get(image_url)  # посылаю запрос по адресу картинки
        file.write(resp.content)

