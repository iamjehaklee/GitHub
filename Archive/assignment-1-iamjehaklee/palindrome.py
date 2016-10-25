def isPalindrome(s):
    s = s.lower()
    x = 0
    y = len(s)
    #Check for an even number of characters in string
    if len(s) % 2 == 0:
        if x == 0 and y == 0 and s == "":
            print('This is a palindrome.') 
        elif s[x] == s[y-1]:
            x = x + 1 
            y = y - 1 
            isPalindrome(s[x:y])
        else:
            print('This is not a palindrome.')
    #Check for an odd number of characters in string            
    if len(s) % 2 != 0:
        if x == 1 and y == 0:
            print('This is a palindrome.')             
        elif s[x] == s[y-1]:
            x = x + 1 
            y = y - 1 
            isPalindrome(s[x:y])
        else:
            print('This is not a palindrome.')

inputStr = input("Enter a string: ")
if isPalindrome(inputStr):
    pass
else:
    pass



