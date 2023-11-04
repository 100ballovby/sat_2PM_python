text = input('Сообщение: ')
shift = int(input('Сдвиг: '))
encrypted_text = ''

for char in text:
    if char.isalpha():  # убеждаемся в том, что символ является буквой
        shift_amount = shift % 26  # убеждаемся, что сдвиг находится в пределах алфавита
        if char.islower():
            shifted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
        else:
            shifted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        encrypted_text += shifted_char
    else:  # если мы работаем с пробелом или знаками препинания
        encrypted_text += char

print(f'Text: {text}')
print(f'Encrypted text: {encrypted_text}')


