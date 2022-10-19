from math import sqrt




while True:
    calculator_display = int(input('''
Pythagoras Calculator:
1. Find the length of A given B and C
2. Find the length of B given A and C
3. Find the length of C given A and B
>>>>>>>
'''))

    if calculator_display == 1:
        side_b = int(input("Side B "))
        side_c = int(input("Side C "))
        side_a = float(sqrt((side_c * side_c) - (side_b * side_b)))
    print(f"The result of side A is {side_a}")

    leve_message= str(input("Do you want to leve YES or NO "))
    if leve_message == "YES":
        break