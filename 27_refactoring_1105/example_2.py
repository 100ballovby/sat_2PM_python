# включение словаря
dict_ = {x: x * x for x in range(8) if x % 2 == 0}

# включение множества
set_ = (x * x for x in range(8))

print(dict_)
print(*set_)
