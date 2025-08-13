'''Palindrome Checker: Write a function to determine if a given string is a palindrome 
(reads the same forwards and backwards). Ignore spaces, punctuation, and 
capitalization. '''
def is_pal(s):
    i,j=0,len(s)-1
    is_palindrome = True
    while i<j:
        if s[i]!=s[j]:
            is_palindrome=False
            break
        i+=1
        j-=1
    if is_palindrome:
        print("Yes") 
    else:
        print("No")

s = input("Enter A String to  if its Palindrome or not : ")
is_pal(s)


