number = 1
while number < 100:
    print("here")
    square_number = number ** 2
    number += 1
    if square_number > 2000:
        break
    print(square_number)