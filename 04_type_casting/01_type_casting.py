# type Casting :

# Type Casting is used to convert value's data type in to another data type 

# Why We need type Casting ?

# Sometime value receives data in type ,but we need to use it  as another type .

# we can use this for change the datatype .


# 1. int()



# Implicit
a=120.2
b=122

print(a+b)


# Explicit
a=input("Enter Any Integer Number :")
b=input("Enter Any Integer Number : ")

print(int(a)+int(b))


print("Second Example")


# Implicit
teacher=120
student=1.5


print(teacher+student)


# Explicit
teacher=input("Enter Any Integer Number : ")
Student=input("Enter Any Integer Number : ")

print(int(teacher)+int(Student))




print("3rd Example")


# Implicit
Kajukatri=120
Modak=30

print(Kajukatri+Modak)


# Explicit
Chintu=int(input("Enter Any Integer Value : "))
Mintu=int(input("Enter Any Integer Value"))


print(Chintu+Mintu)




# 2. FLoat 
print("FLoat Data type casting")

print("1st Example")


# Implicit
a=120.4
b=123


print(a+b)


# Explicit
Shopkeeper=input("Enter Your  Float Value : ")
Customer=input("Enter Your Float Value : ")

print("Total",float(Shopkeeper)+float(Customer))



print("2nd Example")



# Implicit
c=120.3
d=12


print(c+d)


# Explicit
Teacher=float(input("Ener Any Float Number : "))
Student=float(input("Enter Any Float Number : "))


print(Teacher+Student)



print("3rd Example")



# Implicit
car=123.8
truck=225.5

print(car+truck)


# Explicit
Car=float(input("Enter Any Float Number : "))
Truck=float(input("Enter Any FLoat Number :"))

print(int(Car)+int(Truck))



# 3.  String Data type
print("String Data Type Casting")


print('1st Example')

Name="Jayrajsinh"

print(Name)



# Explicit
a=input("Enter Any Value :")
b=input("Enter Any Value :")


print(int(a)+int(b))




print("2nd Example")


# Implicit
Collage="Swarnim University"

print(Collage);



 #. Explicit
c=int(input("Enter Any Integer Number :"))
d=int(input("Enter Any Integer Number :"))

print(str(c)+str(d))





print("3rd Example")



# Implicit
Fav_Seriese="Stranger Things"

print(Fav_Seriese)



# Explicit
x=float(input("Enter Any FLoat Number : "))
y=float(input("Enter Any Float Number : "))

print(str(x)+str(y));



# 4. Boolean 
print("1st Example")



# Implicit
Car=True

print(Car)



# Explicit
Bus=True

print(int(Bus))



print("2nd Example")



# Implicit
Truck=False


print(Truck)



# Explicit
a=int(input("Enter Any Integer Number :"))


print(bool(a))



print("3rd Example")



# Implicit
Mobile=False

print(Mobile)



# Explicit
c=float(input("Enter Any Float Number:"))

print(bool(c))



# 5. List
print("1st Example")



# Implicit
Name=['Jayraj','Neev']

print(Name , type(Name))


# Explicit
Name=['Neev,Jayrajsinh','Meet']


print(bool(Name))




print("2nd Example")



# Implicit
Fruits=['Watermalon','Apple','Banana']


print(Fruits)


# Explicit
print(bool(Fruits))



print("3rd Example")



# Implicit

print(str(car))



print("3rd Example")



# Implicit
Vegetable="Carrot","Cucumber","potato"

print(Vegetable)


# Explicit
print(list(Vegetable))


# 6. Tuple
print("1st Example")



# Implicit
Fruits=('Chiku','Mnago','Apple')

print(Fruits)

# Explicit
print(list(Fruits))



print("2nd Example")



# Impicit
Collage=('GMIT','SSCCM','SSCCS')

print(Collage)



# Explicit
print(list(Collage))



print("3rd Example")


# Implicit
Bike=('BMW','ZX10R','H2R')

print(Bike)



# Explicit
print(bool(Bike))



# 7. Set 


print("1st Example")

# Implicit

Mobile={"Iphone","samsung ","Vivo"}


# Explicit

print(bool(Mobile))





print("2nd Example")


# Implicit


City={'Bhavnagar','Ahmedabad','Surat'}

print(City)

# Explicit

print(tuple(City))




print("3rd Example")


# Implicit

State={"Gujrat","Maharastra","Madhya Pradesh"}

print(State)

# Explicit

print(list(State))



# 8. Dictionary

print("1st Example")


# Implicit

a={
    "Name":"Meet",
    "Age" : "20",
}

print(a)

# Explicit

print(list(a))




print("2nd Example")


# Implicit

b={
    "Name":"Neev",
    "Age" : "18"
}

print(b)

# Explicit

print(tuple(b))




print("3rd Example")

# implicit

c={
    "Cource":"Career X Ai",
    "GR ID" : "13624"
}

print(c)


# Explicit

print(set(c))



# 9. None


x=None


print(x)


print(bool(x))