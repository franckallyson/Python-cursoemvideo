print('='*30)
print('     10 TERMOS DE UMA P.A')
print('='*30)
a1 = int(input('Enter the first term of the PA:'))
r = int(input('Enter the reason of the PA:'))
n = 0
for c in range(1, 11):
    n = a1 + (c - 1) * r
    print(n, end=' → ')
print('END')
