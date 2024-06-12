#How can you check if a string is a palindrome?

#Run a loop from starting to length/2 and check the first character to the last character of the string and second to second last one and so on …. If any character mismatches, the string wouldn’t be a palindrome.

# function to check string is
# palindrome or not
def isPalindrome(str):
 
    # Run loop from 0 to len/2
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
 
# main function
s = "madam"
ans = isPalindrome(s)
 
if (ans):
    print("Yes")
else:
    print("No")