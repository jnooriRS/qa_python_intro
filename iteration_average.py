math_result = int(input("What is your Math reult "))
english_result = int(input("What is your English reult "))
ict_result = int(input("What is your ICT reult "))

set_of_results = (math_result, english_result, ict_result)
average_mark = sum(set_of_results) / len(set_of_results)
print(f"The average grade for all three exams you sat is {average_mark}")

