""" Write a Python program to get a single string from two given strings, 
separated by a space and swap the first two characters of each string."""

str1 = input("enter first string : ")
str2 = input("enter second string : ")
print("before swap :",str1,"",str2)
new_str1 = str2[:2] + str1[2:]
new_str2 = str1[:2] + str2[2:]
print("after swap : ",new_str1," ",new_str2)

