"""Write a Python function that takes a list of words and returns the length of the longest one. """

name = ['sanket','dipak','dip']
max_length = 0
for word in name:
    if len(word) > max_length:
        max_length = len(word)
        print("list of name : ",name,'',"and name in max lenght is : ",max_length)


