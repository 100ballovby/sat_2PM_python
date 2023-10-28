phrase = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ultricies sem nec turpis ornare tincidunt. Mauris eros ipsum, blandit sed purus id, sollicitudin faucibus justo. Quisque sit amet consectetur libero, at dignissim ex. Integer nec velit leo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Duis ultrices tincidunt urna convallis luctus. '


"""Хочу посчитать количество знаков препинания"""
count = 0
for i in range(len(phrase)):
    #if phrase[i] in '.!,?':
    if phrase[i] == ',' or phrase[i] == '.' or phrase[i] == '!' or phrase[i] == '?':
        count += 1

print(f'В этой строке {count} знаков препинания.')
