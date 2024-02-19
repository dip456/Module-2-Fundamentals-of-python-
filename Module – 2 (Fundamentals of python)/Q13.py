"""Write a Python program to count the number of characters (character frequency) in a string """
string = input("enter string : ")
l = list(string)
#print(l)
freq = [l.count(element)for element in l]
#print(freq)
d =dict(zip(l,freq))
print(d)
        


