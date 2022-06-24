n = int(input('Enter a integer number:'))
mult = 0
for c in range(1, n + 1):
    if n % c == 0:
        mult += 1
if mult == 2:
    print("Is a PRIME NUMBER. It's only divisible by 1 and by itself .")
else:
    print("It's NOT a Prime Number. Have {} Dividers.".format(mult))