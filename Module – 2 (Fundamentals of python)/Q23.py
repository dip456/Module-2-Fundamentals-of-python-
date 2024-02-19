"""Write a Python function to insert a string in the middle of a string. 
"""
# string = "hello sir my name is dipak"
# lefts = string[:10]
# right = string[9:]
# add = "good morning"
# new_string = lefts + add + right
# print(new_string)

str1 = "hello how are you"
lefts = str1[:6]
right = str1[5:]
add = input("enter you name : ")
new_string = lefts + add + right
print(" ",new_string)
