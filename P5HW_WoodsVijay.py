#Vijay woods
#11/16/2023
#using if/else, loop, functions and random numbers
import random

def show_menu():
    print("Welcome to Math Quiz")
    print("MAIN MENU")
    print("---------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit Program")

def adding():
    my_sum = random.randint(0,10)+ random.randint(0,10)
    print(" The sum is :", my_sum)
    return my_sum
def subtracting ():
    my_diff = random.randit(0,10)- random.randit(0,10)
    print(" The difference is", my_diff)
    return my_diff

def guessing(guess,value):
     while guess != value:
       if guess > value:
          print("Your guess is too high")
          guess = int(input( " Enter your guess: "))
   
       else:
          print("Your guess is too low")
          guess = int(input( " Enter your guess: "))
    print("Congratulations , your guess is correct !")

#Main function that runs the program
def main():
    while True:
    show_menu()
    user_choice = int(input("Please choose one of the menu options:"))
    if user_choice == 1:
       value = adding()
       guess = int(input( " Enter your guess: "))
       guessing(guess, value)
      
               
    if user_choice == 2:
       value = subtracting ()
       guess = int(input( " Enter your guess: "))
       guessing(guess, value)
       
       if user_choice == 3:
        print(" The program has ended.")
        break
    
#Call the main function
if __name__ == "__main__":
    main()
    
