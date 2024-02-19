""" Write a Python program to count the occurrences of each word in a given sentence"""

string = input("enter string : ")
string = string.split()
word = 0
count = 0 
while(word<len(string)):
    count = 0
    for char in string:
        if string[word] == char:
            count = count + 1
            print(string[word],"present",count,"times")
            word = word +1


