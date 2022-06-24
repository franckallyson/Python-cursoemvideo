from datetime import date
year = int(input('Enter a Year. Enter 0 to analyze the current year.'))
if year == 0:
    year = date.today().year
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('This IS a Leap Year!')
else:
    print('This IS NOT a Leap Year!')
