def sum():
    first_num = float(input('Please enter your first number: '))
    second_num = float(input('Please enter your second number: '))
    sum = first_num + second_num
    print(f'The sum of both numbers is: {sum}')
    return sum

def substract():
    first_num = float(input('Please enter your first number: '))
    second_num = float(input('Please enter your second number: '))
    substract = first_num - second_num
    print(f'The substraction of both numbers is: {substract}')
    return substract

def multiply():
    first_num = float(input('Please enter your first number: '))
    second_num = float(input('Please enter your second number: '))
    multiply = first_num * second_num
    print(f'The multiplication of both numbers is: {multiply}')
    return multiply

def division():
    first_num = float(input('Please enter your first number: '))
    second_num = float(input('Please enter your second number: '))
    division = first_num / second_num
    print(f'The division of both numbers is: {division}')
    return division

run = True

while run:
    print('Welcome to math class! \nPlease enter what would you like to do:')
    print('For sum of 2 numbers, enter +.')
    print('For subsctraction of 2 numbers, enter -.')
    print('For multiplication of 2 numbers, enter *.')
    print('For division of 2 numbers, enter /.')

    user_selection = input()

    if user_selection == '+':
        sum()
        run = False
    elif user_selection == '-':
        substract()
        run = False
    elif user_selection == '*':
        multiply()
        run = False
    elif user_selection == '/':
        division()
        run = False
    else:
        print('Incorrect method choosen.')


