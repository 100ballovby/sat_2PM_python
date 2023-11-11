text = input('Сообщение: ')
shift = int(input('Сдвиг: '))
encrypted_text = ''

for char in text:
    if char.isalpha():  # убеждаемся в том, что символ является буквой
        shift_amount = shift % 32  # убеждаемся, что сдвиг находится в пределах алфавита
        if char.islower():
            shifted_char = chr(((ord(char) - ord('а') + shift_amount) % 32) + ord('а'))
        else:
            shifted_char = chr(((ord(char) - ord('А') + shift_amount) % 32) + ord('А'))
        encrypted_text += shifted_char
    else:  # если мы работаем с пробелом или знаками препинания
        encrypted_text += char

print(f'Text: {text}')
print(f'Encrypted text: {encrypted_text}')



