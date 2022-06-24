phrase = str(input('Enter a phrase:')).strip().upper()
phrase_normal = phrase.replace(' ', '')
phrase_reverse = phrase_normal[::-1]
print('The inverse of {} is {}!'.format(phrase_normal, phrase_reverse))
if phrase_normal == phrase_reverse:
    print('The phrase is a palindrome.')
else:
    print('The phrase is not a palindrome.')
