#Vijay woods
#10/10/23
#Working with lists

#Create variables and get user input(6)
num_grades = int(input("How many grades will you enter? "))
#Create empty list
grade_list = []

for grade in range(num_grades):
    this_grade = int(input("Enter a grade: "))
    
    while this_grade < 0 or this_grade > 100:
        print("Invalid grade entered.")
        this_grade = int(input("Enter a grade: "))
        
    grade_list.append(this_grade)
    print(f"{this_grade} has been added to the list")
    
for grade in grade_list:
    print(grade)




print(grade_list)


max_value = max(grade_list)
min_value = min(grade_list)

sum_value=sum(grade_list)
average=sum_value/len(grade_list)
print("Max: ", max_value)
print("Min:", min_value)
print("Sum:",sum_value)
print("Average:",average)


