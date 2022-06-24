wage = float(input('Enter your salary:'))

#Jeito Simplificado \/
#inc = wage * 0.15 if wage <= 1250 else wage * 0.10

#Jeito normal \/
if wage <= 1250:
    inc = wage * 0.15
else:
    inc = wage * 0.10
all = wage + inc
print('Your increase was U${:.2f} and your new salary is U${:.2f}'.format(inc, all))
