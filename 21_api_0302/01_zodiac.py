from functions import translate_from_english, get_horo


zodiacs = {
    'Овен': 'Aries',
    'Телец': 'Taurus',
    'Близнецы': 'Gemini',
    'Рак': 'Cancer',
    'Лев': 'Leo',
    'Дева': 'Virgo',
    'Весы': 'Libra',
    'Скорпион': 'Scorpio',
    'Стрелец': 'Sagittarius',
    'Козерог': 'Capricorn',
    'Водолей': 'Aquarius',
    'Рыбы': 'Pisces',
}
sign = input('Знак зодиака: ').capitalize()

horoscope = get_horo(zodiacs[sign])
translation = translate_from_english(horoscope)

print(translation)