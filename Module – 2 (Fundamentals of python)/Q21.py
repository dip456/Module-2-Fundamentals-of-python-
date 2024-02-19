"""Write a Python function to reverses a string if its length is a multiple of 4. """

string = input("enter string : ")

if len(string) % 4 == 0:
    reversed_string = string[:-1]
    print("Reversed String:", reversed_string) 
else:
    print("String length is not a multiple of 4. Original String:",string)

