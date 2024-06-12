#How can you count the number of occurrences of a substring within a string?

#string count() used to count the number or occurrences in substring.

var1 = "Hey I am a professional MERN stack developer. I am pursuing Data science forrm Ducat"
string1 = var1.count('a')
print(string1)

#Using String Count() to Count Occurrences of Character in Multiple String
var2 = ["Java", "Javascript", "Python"]
string2 = 'a'
total_count = sum(string.count(string2) for string in var2)
print(total_count)