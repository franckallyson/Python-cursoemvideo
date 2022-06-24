def factorial(n, show=False):
    '''
    -> Calculates the factorial of a number.
    :param n: Number to be calculated.
    :param show: (Optional) Show or not show the calculation.
    :return: The factorial value of a number 'n'.
    '''
    from math import factorial
    if show:
        for c in range(n, 0, -1):
            if c == 1:
                print(f'{c} = ', end='')
            else:
                print(f'{c} x ', end='')
    return factorial(n)


# Main Program
print(factorial(10, True))
help(factorial)
