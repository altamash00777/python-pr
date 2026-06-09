# loop use to print something multiple time without writing 
# it manually multiple time

# three -> for while do-while
# ---------------------------------------------
# while condition:
#      code

# count = 1

# while count<=5:
#     print("hello")
#     count=count+1

# count = 1

# while count<=5:

#  num1=int(input("enter num"))
#  num2=int(input("enter num"))
#  sum=num1+num2

#  print(num1+num2)

#  count=count+1 

# printing 1 to n

# num=1

# while num<=10:
#     print(num)
#     num=num+1

# -----------------------------------------------


# for loop

# for i in range(5):
#  print(i)

#sumof 100

# total=0

# for i in range(1,101):
#        total=total+i

# print(total)

# printinf even from 1 to 50

# for i in range(1,51):
#     if i%2==0:
#         print(i)


# Ask a number from user and print:

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# ...

# Rules:

# multiple of 3 → Fizz
# multiple of 5 → Buzz
# both → FizzBuzz


for i in range(1,11):
    if i%3==0 and i%5==0:
        print("fizzbuzz")
    elif i%3==0:
        print("buzz") 
    elif i%5==0:
        print("buzz")
    else: 
        print(i)
