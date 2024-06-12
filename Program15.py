#how do you check if a string conatining only numeric characters

#Python String isalpha() method is used to check whether all characters in the String are an alphabet.
var1 = "23453243243"
string1 = var1.isnumeric()
print(string1)
#output True

#using whitespace
var2 = "My name is Rishabh Pratap 005"
string2 = var2.isnumeric()
print(string2)
#Output False