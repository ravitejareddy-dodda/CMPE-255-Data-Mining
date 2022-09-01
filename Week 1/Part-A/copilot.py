#program to check if the email is valid or not
import re
email = input("Enter your email: ")
if(re.search("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email)):
    print("Valid email")
else:
    print("Invalid email")

#program to sort the numbers in the list
numbers = [1, 3, 4, 2]
numbers.sort()
print(numbers)

#program check the strength of the password
import re
password = input("Enter your password: ")
if(re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password)):
    print("Strong password")
else:
    print("Weak password")

#program to check if the year is leapyear or not
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))     
else:
    print("{0} is not a leap year".format(year))

#program to check if the number is positive or negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#program for simple calculator
#ADDITION
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
#SUBSTRACTION
difference = float(num1) - float(num2)
print('The difference of {0} and {1} is {2}'.format(num1, num2, difference))
#MULTIPLICATION
product = float(num1) * float(num2)
print('The product of {0} and {1} is {2}'.format(num1, num2, product))
#DIVISION
quotient = float(num1) / float(num2)
print('The quotient of {0} and {1} is {2}'.format(num1, num2, quotient))
#REMINDER
remainder = float(num1) % float(num2)
print('The remainder of {0} and {1} is {2}'.format(num1, num2, remainder))

#program to find the largest number among the three input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
    largest = num1
elif (num2 >= num1) and (num2 >= num3):
    largest = num2
else:
    largest = num3
print("The largest number between",num1,",",num2,"and",num3,"is",largest)

#program to check the data type of the input values
a = 5
print(type(a))
b = 2.0
print(type(b))
c = 1+2j
print(type(c))
d = 1,2,3,4
print(type(d))
e = [5,6,7,8]
print(type(e))
f = {9,10,11,12}
print(type(f))
g = {13:14,15:16}
print(type(g))
h = True
print(type(h))





