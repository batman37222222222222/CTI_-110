# Vijay Woods
# 10/5/2023
# Dictionaries


#Get input from user
name= input("Enter your name: ")
hair= input("Enter your hair color: ")
eye = input("Enter your eye color: ")
height = float(input("Enter height as a decimal: "))
age= int(input("Enter your age: "))
food= input(" What's your  favorite food?: ")

#Create a dictionary- curly braces
my_dict = {"Name": name, "Hair_color": hair, "Eye_color" : eye,"Height":height, "Age":age, "Food":food}

#Get values using the key
print(f"{my_dict['Name']} is a {my_dict['Height']} tall student with{my_dict['Eye color']}They are{my_dict['Age']}and their favorite{my_dict['Food']}.")
