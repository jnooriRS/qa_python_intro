min_varaible = 66
max_variable = 100
counter = 0
while counter < 3:
    user_guess=(int(input("What is your guess >>> ")))
    if user_guess > min_varaible or user_guess == max_variable:
        break
    else:
        counter = counter +1
        if counter == 1:
            print(f"Bad luck do try again- you have had {counter} guess out of 3")
        else:
            print(f"Bad luck do try again- you have had {counter} guesses out of 3")

