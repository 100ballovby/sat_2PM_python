string = input("Enter: ")
tmp = string.split()

for i in range(len(tmp)):
    tmp[i] = tmp[i][::-1]

string = ' '.join(tmp)
print(string)




