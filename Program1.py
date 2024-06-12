#How to concatenate two string in python?
#There are multiple way to concatenate two or more string in python

#lets concatenate using '+' operator
firstName = "Rishabh"
secondName = " Pratap"

myName = firstName + secondName
print(myName)

#now concatenate using joining() method

companyName = "rishabhtech"
domainName = ".com"

website = "".join([companyName, domainName])
print(website)