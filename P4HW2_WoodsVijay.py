#Vijay Woods
#10/26/23
#Uses if/else statements
employeename = input("Enter your employee name: ")
 
while employeename != "Done":
        #Get employee name from user
       
        #Get number of hours from user
        hours = int(input("numbers of hours: "))
        #Get payrate per hour from user
        payrate= float(input(" Enter payrate per hours: "))
        #Determine if employee worked more than 40 hours
        #Calculate reg hours worked
        #Calculate OT hours
        if hours > 40:
            OT= hours - 40

            reghours = 40
        else:
            OT = 0
            reghours = hours


        #Calculate OT Pay
        OTpay  = OT*(payrate*1.5)
        regpay = reghours*(payrate)
        # Display name, payrate, reg hours, OT hours, gross pay
        print("Name: " ,employeename)
        print("Payrate: " , payrate)
        print("Reghour: " , reghours)
        print("Regpay: ",  regpay)
        print("OThours : ", OT)
        print("OTpay: ", OTpay)
        print("grosspay", regpay + OTpay)
        employeename = input("Enter your employee name: ")
