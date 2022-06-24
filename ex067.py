while True:
    print('--'*20)
    print('Multiplication Table')
    print('--'*20)
    n = int(input('Enter a Number(Negative to Stop):'))
    if n < 0:
        break
    for c in range(0, 10):
        print(f'{n:2} X {c:2} = {n * c:2}')
print('End of Section')
