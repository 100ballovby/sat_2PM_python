shop = {
    'milk': 1.29,
    'oil': 6.99,
    'cookies': 0.75,
    'banana': 4.56,
    'orange': 6.77
}
print(shop['banana'])
shop['banana'] = 10.1  # замена значения
print(shop)
shop['grape'] = 9.65  # добавлять можно только пару
print(shop)

# ЗАМЕНА КЛЮЧЕЙ НЕВОЗМОЖНА МЕНЯТЬ МОЖНО ТОЛЬКО ЗНАЧЕНИЕ
for key in shop.keys():  # получить все ключи словаря
    print(f'Key: {key}')

for value in shop.values():  # получить все значения словаря (без ключей)
    print(f'Value: {value}')

for key, value in shop.items():
    print(f'Key: {key}, Value: {value}')


