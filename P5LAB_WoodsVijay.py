#Vijay Woods
#10/19/2023
#Working with nested if/else statements

def get_year():
#Get year from user
   year= int(input("Enter a year to determine if its a leap year: "))
   return year
def divide_by_4(year):
   if year % 4 == 0:
      return True
   else:
      return False
def divide_by_100(year):
   if year % 100 == 0:
      return True
   else: 
      return False
         
def divide_by_400(year):
   if year % 400 == 0:
      return True
   else:
      return False

def output_results(leap_status, year):
   if leap_status == True:
    print(f"The year {year} is a leap year")
   else :
    print(f"The year {year} is NOT a leap year")
    

def  main():
#Create a boolean variable to hold leap year status
   is_leap= False

   year = get_year()

   if divide_by_4 (year):                   #Does year divide by 4
      if divide_by_100(year):           #Does year divide by 100
        if divide_by_400(year):           #Does year divide by 400
            is_leap = True
        else :
            is_leap = False    #Does NOT year divide by 400
      else :
            is_leap = True    #Does NOT year divide by 100
   else :
         is_leap = False   #Does NOT year divide by 4
           #Print output to user
   output_results (is_leap, year)
#Call the main function
main()
