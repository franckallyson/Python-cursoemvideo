phrase = str(input('Enter a phrase:')).strip().lower()

amount = phrase.count('a')
find = phrase.find('a')
find_last = phrase.rfind('a')

print('The amount of "A": {}'.format(amount))
print('The first "A" is in position: {}'.format(find + 1))
print('The last "A" is in position: {}'.format(find_last + 1))
