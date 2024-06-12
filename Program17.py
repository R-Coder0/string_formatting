#How can you reverse the string in python 

#we call a function to reverse a string, which iterates to every element and intelligently joins each character in the beginning so as to obtain the reversed string.  
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = "ArtificialIntellegence"
 
print("The original string is : ", end="")
print(s)
 
print("The reversed string(using loops) is : ", end="")
print(reverse(s))