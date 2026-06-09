# function is block of code that help to write specific task 
# single time and later we can use them again

# def welcome():
#     print("function")

# welcome()
# welcome()
# welcome()
# welcome()


# def greet():
#     print("hello altamahs")
#     print("what going in your life")

# greet()
# greet()

# function with parameters

# def student(name):
#     print("name is ",name)

# student("altamash")


# def student(name,age):
#     print("name-> ",name)
#     print("age-> ",age)

# student("altamash",20)

# return keyword use to send value
# back to

# def sum(a,b):
#     return a+b

# result=sum(20,30)

# print(result)


# def sub(a,b):
#     return a-b

# result=sub(23,33)

# print(result)

# default parameter
# in default parameter we pass value inside fun 
# by default if we not pass any value
# it will return that

# def greet(name="guest"):
#     print("name is ",name)

# greet("altamash")
# greet() 


# def intro(name,age):
#     print("name is ",name ,"age is ",age)

# intro(name="altamash" , age=32)

num1=int(input("enter number 1st : "))
num2=int(input("enter number 2nd : "))

def add(num1,num2):
   return num1+num2

def sub(num1,num2):
   return num1-num2

def multi(num1,num2):
   return num1*num2

def div(num1,num2):
   return num1/num2


print("choose operation")
print("1 Add")
print("2 Sub")
print("3 Multi")
print("4 Div")

choice = int(input("enter choice"))

if choice == 1:
   print("sum is ",add(num1,num2))
elif choice == 2:
   print("sub is ",sub(num1,num2))
elif choice == 3:
   print("multiply is ",multi(num1,num2))
elif choice == 4:
   print("div is ",div(num1,num2))
else:
   print("invalid")

