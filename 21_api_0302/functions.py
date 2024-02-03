import requests


def translate_from_english(text):
    url = "https://deep-translate1.p.rapidapi.com/language/translate/v2"

    payload = {
        "q": text,
        "source": "en",
        "target": "ru"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "deep-translate1.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers).json()
    return response['data']['translations']['translatedText']


def get_horo(sign):
    url = "https://daily-horoscope-api.p.rapidapi.com/api/Daily-Horoscope-English/"

    querystring = {
        "zodiacSign": sign,
        "timePeriod": "tomorrow"
    }

    headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "daily-horoscope-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    return response['prediction']


