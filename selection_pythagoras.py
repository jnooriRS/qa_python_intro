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
        side_a = round(sqrt((side_c * side_c) - (side_b * side_b)), 2)
        print(f"The result of side A is {side_a}")

    elif calculator_display == 2:
        side_a = int(input("Side A "))
        side_c = int(input("Side C "))
        side_b = round(sqrt((side_a * side_a) - (side_c * side_c)), 2)
        print(f"The result of side A is {side_b}")
    
    elif calculator_display == 3:
        side_a = int(input("Side A "))
        side_b = int(input("Side B "))
        side_c = round(sqrt((side_a * side_a) - (side_b * side_b)), 2)
        print(f"The result of side C is {side_c}")

    leve_message= str(input("Do you want to leve YES or NO ")).upper()
    
    if leve_message == "YES":
        break

    # sqrt = squre root as we need to reverse result square

    #https://www.youtube.com/watch?v=JCG4HHGVqiY