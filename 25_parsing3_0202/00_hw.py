import bs4
import requests as req
import json


url = 'https://selectel.ru/blog/courses/'
st_accept = "text/html"  # говорим серверу, что хотим получить html
st_useragent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
headers = {
	"Accept": st_accept,
	"User-Agent": st_useragent,
}
page = req.get(url, headers=headers)
soup = bs4.BeautifulSoup(page.content, 'lxml')

courses = soup.findAll('li', attrs={'class': 'info-page_material-item'})
courses_info = {}
for course in courses:
	link = course.find('a', attrs={'class': 'course-card'})
	name = course.find('h3', attrs={'class': 'course-card_title'})
	try:
		course_name = name.text.strip()
		course_link = link.get('href')
		courses_info[course_name] = {'course_link': course_link}
	except AttributeError as e:
		print(f'Link: {link} raised error: {e}')


for course in courses_info:
	url = courses_info[course]['course_link']
	st_accept = "text/html"  # говорим серверу, что хотим получить html
	st_useragent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
	headers = {
		"Accept": st_accept,
		"User-Agent": st_useragent,
	}
	page = req.get(url, headers=headers)
	soup = bs4.BeautifulSoup(page.content, 'lxml')

	description = soup.find('p', attrs={'class': 'course-detailed-about_text'})
	course_program = soup.findAll('li', attrs={'class': 'course-detailed-about_program-item'})
	course_program_list = []
	for element in course_program:
		element_heading = element.find('a', attrs={'class': 'course-detailed-about_program-subtitle'})
		element_description = element.find('p', attrs={'class': 'course-detailed-about_program-text'})
		course_program_list.append([element_heading.text.strip(), element_description.text.strip()])
	courses_info[course].update({'description': description.text.strip()})
	courses_info[course]['course_program'] = course_program_list

with open('selectel.json', 'w') as file:
	file.write(json.dumps(courses_info, indent=4, ensure_ascii=False))


