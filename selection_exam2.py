mark_input =int(input("Student mark >>>>"))
level_inpt =int(input("Is it level 1 or 2 >>>"))
while True:
    if (level_inpt == 1):
        if mark_input < 1 or mark_input > 100:
            print("Error: marks must be between 1 and 100")
        elif mark_input < 50:
            print("Fail")
        elif mark_input == 50 or mark_input < 61:
            print("Pass")
        elif mark_input == 61 or mark_input < 71:
            print("Merit")
        else:
            print("Distinction")
    elif(level_inpt == 2):
        if mark_input < 1 or mark_input > 100:
            print("Error: marks must be between 1 and 100")
        elif mark_input < 40:
            print("Fail")
        elif mark_input == 40 or mark_input < 51:
            print("Pass")
        elif mark_input == 51 or mark_input < 66:
            print("Merit")
        else:
            print("Distinction")
    continue_calculation = input("Let's do next calculation? (yes/no): ")
    if continue_calculation == "no":
        break