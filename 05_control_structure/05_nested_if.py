Age=18

Drivinglicense=True


if (Age>=18):
    if (Drivinglicense==True):
        print("You can drive the vehicle")
    else:
        print("You have to register for driving license after that you can drive the vehicle.")
else:
    print("You are Minor Citizen")



Age=int(input("Enter Any Number : "))

Pention=True

if (Age>=50):
     if (Pention==True):
         print("You are senior Citizen")
     else:
         print("You Have to work for the family")
else:
    print("You Are not Senior citizen")