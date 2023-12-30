import os


def find_and_run_file(file_name):
    for root, dirs, files in os.walk("."):
        for file in files:
            if file == file_name:
                os.system(f'python {os.path.join(root, file)}')


find_and_run_file('file8.py')