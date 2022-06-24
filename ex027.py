name = str(input('Enter your name: ')).strip()

List = name.rsplit()
name1 = List[0]
name2 = List[len(List) - 1]

print('Nice to meet you!')
print('Your first name is {}'.format(name1.capitalize()))
print('Your last name is {}'.format(name2.capitalize()))
