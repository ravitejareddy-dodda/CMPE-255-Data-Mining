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

#check if the number is positive or negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#program for simple calculator
#addition
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
#add two numbers
sum = float(num1) + float(num2)
#subtract two numbers
difference = float(num1) - float(num2)
#multiply two numbers
product = float(num1) * float(num2)
#divide two numbers
quotient = float(num1) / float(num2)
#remainder of two numbers
remainder = float(num1) % float(num2)
#display the sum
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
#display the difference
print('The difference of {0} and {1} is {2}'.format(num1, num2, difference))
#display the product
print('The product of {0} and {1} is {2}'.format(num1, num2, product))
#display the quotient
print('The quotient of {0} and {1} is {2}'.format(num1, num2, quotient))
#display the remainder
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
