import os
import random as r


code = """
def func():
    print('Hello, World!')
    
if __name__ == '__main__':
    func()
"""
new_path = os.path.dirname(os.path.realpath(__file__))
print(new_path)
os.mkdir(os.path.join(new_path, 'koshmar'))

# os.path.join - позволяет собрать путь к файлу
for i in range(10):
    with open(os.path.join(new_path, 'koshmar', f'file{i}.py'), 'w') as file:
        file.write(code)



