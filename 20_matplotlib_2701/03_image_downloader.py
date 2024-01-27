import requests as req

url = 'https://www.shutterstock.com/image-photo/rear-view-dad-holding-her-600w-2206914231.jpg'
with open('image.jpg', 'wb') as f:
    resp = req.get(url)
    f.write(resp.content)

