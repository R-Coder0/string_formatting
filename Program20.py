#How can you remove specific characters from a string in Python?

#removepreffix() and removesuffix() method use to remove first and last character from string

var1 = "I My name is RIshabh Pratap I "
string1 = var1.removeprefix(" My")
string2 = var1.removesuffix("I ")
print(string1)
print(string2)