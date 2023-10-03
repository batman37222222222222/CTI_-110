#vijay
#Date
#Calculates travel expences

budget=int(input("Enter Budget: "))

dest=input("where are you taveling?")

gas=int(input("Enter gas budget: "))
food=int(input("Enter food budget: "))
hotel=int(input("Enter hotel Budget: "))

expences= gas+food+hotel

print("-----------Travel Expences--------")
print("Location: ", dest)
print("Initial Budget: ",budget)
print()
print("Gas Cost: ",gas)
print("Gas Food:", food)
print("Gas Hotel:",hotel)
print()
print("Remaining Balance: ", budget-expences)
