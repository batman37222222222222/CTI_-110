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


'''
# Create empty list
modules=[]
# Add values to list
modules.append(module1)
modules.append(module2)
modules.append(module3)
modules.append(module4)
modules.append(module5)
modules.append(module6)


print(modules)
# Calculation

max_value = max(modules)
min_value = min(modules)

sum_value=sum(modules)
average=sum_value/len(modules)
print("Max: ", max_value)
print("Min:", min_value)
print("Sum:",sum_value)
print("Average:",average)

'''
