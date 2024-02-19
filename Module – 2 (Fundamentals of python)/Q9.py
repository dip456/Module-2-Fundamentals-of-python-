""" Write a Python program to sum of three given integers. However, if two values are equal sum will be zero."""

num1 = 10
num2 = 20
num3 = 10
if(num1 == num2 or num2 == num3 or num3 ==num1):
    print("sum is zero")
else:
    sum = num1+num2+num3
    print(sum)
