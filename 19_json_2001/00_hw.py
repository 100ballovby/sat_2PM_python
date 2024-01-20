def text_to_array(filename):
    with open(filename, 'r') as f:
        text = f.read()
    text = text.split()
    for i in range(len(text)):
        text[i] = int(text[i])
    return text

print(text_to_array('hw.txt'))
