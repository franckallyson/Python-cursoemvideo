#Variáveis
value = float(input('House Value: R$'))
salary = float(input('Buyer Salary: R$'))
time = int(input('How many years of financing?'))
#Calculos
ins = value / (time * 12)
limit = salary * 0.30
print('The installments will be of {:.2f}'.format(ins))
#Condicionais
if ins > limit:
    print('You cannot pay more than 30% of your salary in installments\n'
          'DENIED Financing ')
else:
    print('APPROVED Financing')
