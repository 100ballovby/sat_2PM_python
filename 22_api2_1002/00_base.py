import requests

url = "https://atmosphere-nitrous-oxide-levels.p.rapidapi.com/api/nitrous-oxide-api"

headers = {
	"X-RapidAPI-Key": "3dbf5c964dmsha4bc11c9413882ep1c54a5jsn910c07577da3",
	"X-RapidAPI-Host": "atmosphere-nitrous-oxide-levels.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

data = response.json()

years = {}
for item in data['nitrous']:
	year = item['date'][:4]
	month = item['date'][5:]
	if year not in years:  # если года нет в словаре с годами
		years[year] = []  # добавляем год и пишем ему список
	else:
		years[year].append({month: {'average': item['average'], 'trend': item['trend']}})
		# в список добавляем данные по месяцам

for year in years:
	with open(f'date_years/{year}.txt', 'w') as file:
		year = years[year]
		for month in year:
			print(month)

# TODO: Необходимо собрать ответ от API. И поместить его в папку с файлами.
#  Каждый файл - это отдельный год. Внутри каждого файла необходимо написать
#  заголовок с месяцем (название), средний показатель содержания оксида азота,
#  тренд показателя содержания оксида азота.
#  Дополнение. Отсортируйте данные таким образом, чтобы выше находились показатели
#  большие по количеству оксида азота.
