from datetime import date
majority = 0
no_majority = 0
for c in range(1, 8):
    birth = int(input("Enter the person's year of birth: "))
    age = date.today().year - birth
    if age < 18:
        no_majority += 1
    elif age >= 18:
        majority += 1
print('{} people HAVE COME of age and {} people HAVE NOT COME of age.'.format(majority, no_majority))
