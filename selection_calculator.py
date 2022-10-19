continue_calculation = ""
while True:
    operation = input('''
Please type in the math operation you would like to complete:
1. + for addition
2. - for subtraction
3. * for multiplication
4. / for division
''')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if operation == '1':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '2':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '3':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '4':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

        # check if user wants another calculation
            # break the while loop if answer is no
    continue_calculation = input("Let's do next calculation? (yes/no): ")
    if continue_calculation == "no":
        break
else:
    print('You have not typed a valid operator, please run the program again.')
        
 

