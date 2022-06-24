man = ''
ageman = 0
woman = 0
s = 0
for people in range(1, 5):
    name = str(input("Enter the person's name: ")).strip().capitalize()
    age = int(input("Enter the person's age: "))
    gender = int(input("Enter the person's gender\n[ 1 ] Male\n[ 2 ] Female\nYour answer:"))
    s += age
    if gender == 1:
        if age > ageman:
            man = name
            ageman = age
    else:
        if age < 20:
            woman += 1
print('The average age of the group is: {:.1f}'.format(s/4))
print('The older man is: {} with {} Years Old'.format(man, ageman))
print('How many woman have under 20 years old: {}'.format(woman))
