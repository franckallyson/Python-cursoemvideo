import random
a1 = input('1° Aluno: ')
a2 = input('2° Aluno: ')
a3 = input('3° Aluno: ')
a4 = input('4° Aluno: ')
list = [a1, a2, a3, a4]
drawn = random.choice(list)
print('-'*25, '\nThe selected student is {}'.format(drawn))
