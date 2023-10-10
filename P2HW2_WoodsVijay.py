#Vijay woods
#10/10/23
#Working with lists

#Create variables and get user input(6)

module1=int(input("Enter grade for module 1:"))
module2=int(input("Enter grade for module 2:"))
module3=int(input("Enter grade for module 3:"))
module4=int(input("Enter grade for module 4:"))
module5=int(input("Enter grade for module 5:"))
module6=int(input("Enter grade for module 6:"))

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

