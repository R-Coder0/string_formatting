#How do you access a substring of a string using slicing?

#Python slicing can be done in two ways:
#Using a slice() method
#Using the array slicing  [:: ] method

# String slicing 
String = 'DATASCIENCE'

# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String slicing using slice() method")
print(String[s1])
print(String[s2])
print(String[s3])

# String slicing
String1 = 'MACHINELEARNING'
 
# Using indexing sequence
print("String slicing using array slicing method")
print(String1[:3])
print(String1[:2:3])
print(String1[1:2:3])



