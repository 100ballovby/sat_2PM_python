import os
import random as r


def file_to_list(filename):
    questions = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            questions.append(line)
    return questions


new_path = os.path.dirname(os.path.realpath(__file__))
os.mkdir(os.path.join(new_path, 'exam'))
questions = file_to_list('2024-01-06_dir/questions.txt')
for i in range(20):
    with open(os.path.join(new_path, 'exam', f'bilet_{i}.py'), 'w') as file:
        q1 = r.choice(questions)
        q2 = r.choice(questions)
        file.write(q1)
        file.write(q2)




