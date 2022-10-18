import statistics

data= "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,1,4,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(",")
updated_list = list(map(int,grades))
# print(updated_list)
updated_list.sort()
#print(updated_list)
min_number= min(updated_list)
#print(min_number)
max_number= max(updated_list)
# print(max_number)
averageGrade = sum(updated_list) / len(updated_list)
averageGrade_2 = (round(averageGrade, 2))
#print(averageGrade_2)
#rint(updated_list)
average_mean = statistics.mean(updated_list)
print(average_mean)
average_median = statistics.median(updated_list)
print(average_median)








#averageGradeQuick = statistics.mean(gradesInt)
#print(averageGradeQuick)

#medianGrade = statistics.median(gradesInt)
#print(medianGrade)