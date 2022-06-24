def vote(y):
    from datetime import date
    age = date.today().year - y

    if age < 16:
        return f'With {age} years old: VOTE DENIED!'
    elif 16 <= age < 18 or age > 65:
        return f'With {age} years old: OPTIONAL VOTE!'
    else:
        return f'With {age} years old: MANDATORY VOTE!'


# Main Program
birth = int(input('What is your birth year?'))
print(vote(birth))
