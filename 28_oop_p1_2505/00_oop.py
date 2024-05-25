class Person:
	def __init__(self, height, weight, gender, s_tone, f_name, l_name):
		"""Метод инициализации. Задает изначальные данные объекту"""
		self.height = height
		self.weight = weight
		self.__age = 0
		self.gender = gender
		self.skin_tone = s_tone
		self.first_name = f_name
		self.last_name = l_name

	def set_age(self, age):  # метод-сеттер, который позволяет назначить значение инкапсулированному параметру класса
		if age - self.__age < 1.9:
			self.__age = age

	def get_age(self):  # метод-геттер, который позволяет ПОЛУЧИТЬ значение инкапсулированного параметра класса
		print(self.__age)

	def say(self, text):
		"""Метод, описывающий поведение экземпляра класа. Теперь он может говорить."""
		print(f'{self.first_name} says: "{text}"')

	def __str__(self):
		return f'Hello! I am {self.first_name} {self.last_name}, {self.__age} years old.'

	def __eq__(self, other):  # метод описывает механизм сравнения экземпляра класса через оператор == с другими методами
		if type(other) == int:
			return self.__age == other
		elif type(other) == str:
			return self.first_name == other
		else:
			return True



egor = Person(0.55, 3.5, 'M', 'White', 'Egor', 'Tsybin')
oksana = Person(0.43, 2.66, 'F', 'White', 'Oksana', 'Jones')
egor.set_age(1.5)
egor.get_age()

egor.say('Hello!')
oksana.say('Goodbye!')
print(egor)
print(oksana)

print(egor == True)
