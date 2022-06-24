ans = 'Yes'
while ans == 'Yes':
    print('-'*40)
    wage = float(input("Enter the employee's salary: U$ "))
    nwage = wage * 1.15
    print("The new employee's salary with 15% increase is U${}".format(nwage))
    print('-'*40)
    ans = str(input('Do you want to do a new search?[Yes/No]'))
else:
    print('End of search!')
