mark_input =int(input("Student mark >>>>"))
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

