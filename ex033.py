n1 = int(input('Enter the 1st Value: '))
n2 = int(input('Enter the 2nd Value: '))
n3 = int(input('Enter the 3rd Value: '))

#Maior
if n1 > n2 and n3:
    larger = n1
if n2 > n1 and n3:
    larger = n2
if n3 > n1 and n2:
    larger = n3
#Menor
if n1 < n2 and n3:
    smaller = n1
if n2 < n1 and n3:
    smaller = n2
if n3 < n1 and n2:
    smaller = n3

print('The larger value is {}'.format(larger))
print('The smaller value is {}'.format(smaller))
