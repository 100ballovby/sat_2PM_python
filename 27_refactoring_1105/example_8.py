students = ['Маша', 'Женя', 'Катя', 'Слава', 'Кирилл']


for i in range(len(students)):
	student = students[i]
	print(f'#{i + 1}: {student}')

# Python-way:
for i, student in enumerate(students, 1):
	print(f'#{i}: {student}')
