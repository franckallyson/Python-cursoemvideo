n = list()
for count in range(0, 5):
    val = int(input(f'Enter the {count}º number:'))
    if count == 0:
        n.append(val)
        print('Insert Value!')
    else:
        if val < n[0]:
            n.insert(0, val)
            print('Insert on the position 0.')
        elif val > n[len(n)-1]:
            n.append(val)
            print('Insert on the last position.')
        else:
            for count2 in range(1, len(n)):
                if n[count2-1] < val < n[count2]:
                    n.insert(count2, val)
                    print(f'Insert on the position {count2}')
print(f'The list in ascending order is {n}')
