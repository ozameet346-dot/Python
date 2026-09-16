# and

# In AND operator has two condition .

# In this operator Each Condition should be True .

age=18

drivinglicense="You can drive the vehicle"

if (age>=18 and drivinglicense):
    print("You can drive the vehicle")

else :
    print("you can't drive the vehicle")   



# 2nd Condition

if (age>18 and drivinglicense):
    print("you can drive the vehicle")  
else :
    print("you can't drive the vehicle")     



age=60

senior="You are senior citizen"

if (age>=60 and senior):
    print("you are senior citizen")

else :
    print("you are not senior citizen")


# 2nd condition

if (age>60 and senior):
    print("you are senior citizen")

else:
    print("you are not senior citizen")



age=18

minor="you are minor"


if (age<=18 and minor):
    print("you are eligable to vote")

else: 
    print("you are not eligable to vote")


    # 2nd condition

if (age<18 and minor):
    print("you are eligable to vote")
else:
    print("you are not eligable to vote")



#  2. Or 

# In OR operator has two condition .

# In this operator one condition is True and second operator is False .


Student_No=1234
teacher="Shivam Sir"

if (Student_No==1234 or teacher=="Shivam Sir"):
    print("Today is Shivam Sir's Lecture")

else :
    print("Today is Janvi Mam's Lecture")


# 2nd Condition 


if (Student_No==5678 or teacher=="Janvi Mam"):
    print("Today is Shivam Sir's Lecture")

else:
    print("Today is Janvi Mam's Lecture")


age>=18
license="Eligable to drive"
license1="Not Eligable"


if (age>18 or license):
    print("You are eligable to drive any vehicle")
else:
    print("You are not eligable to drive any vehicle")

# 2nd condition

if (age<17 or license1=="Eligable to drive"):
    print("You are eligable to drive any vehicle")
else:
    print("You are not eligable to drive any vehicle")


age=60
citizen="Senior"
citizen1="Minor"

if (age>=60 or citizen):
    print("you are senior citizen")
else:
    print("you are not senior citizen")

# 2nd condition

if (age<60 or citizen1=="Senior"):
    print("you are senior citizen")
else:
    print("you are not senior citizen")



# 3. Not 

# In this operator while we use this operator value will define opposite value of it 


Neev=False

print(not Neev)


teacher=True

print(not teacher)


Meet=True

print(not Meet)