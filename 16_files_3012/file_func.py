def read_file(path):
    with open(path, 'r') as f:
        lines = []
        for line in f.readlines():
            lines.append(line)
    return lines


def write_file(path, text):
    with open(path, 'w') as f:
        f.write(text)


def append_file(path, text):
    with open(path, 'a') as f:
        f.write(text)


