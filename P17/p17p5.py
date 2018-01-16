# Psuedocode
##
##def isPalindrome(s): //creates function to check if input is a string
##    '''checks whether a string s is a palindrome'''
##    if type(s) == str: //if input is a string return true otherwise return false
##        print('About to return True from isPalindrome as input is string')
##        return True
##    else:
##        print('About to return False from isPalindrome as input is not string') //test statement
##
##def toChars(s): //converts string to lowercase and removes non-letters
##    '''Converts a string to lowercase and removes non-letters'''
##    s = s.lower() //sets chars in s to lowercase
##    letterstring = ''
##    for c in s:
##        if c in 'abcdefghijklmnopqrstuvwxyz':
##            letterstring += c 
##    print ('About to return letterstring value from toChars') //test statement
##    return letterstring
##
##def isPal(s):
##    '''checks whether string s is a palindrome assumes s is string with only lowercase letters and no non-letters
##    returns True if s is a Palindrome; returns False otherwise. Recrusive function '''
##
##       if len(s) <= 1:
##        print ('About to return True from isPal for the base case') //test statement
##        return True
##    else:
##        print('About to return result s[0] == s[-1] and isPal(s[1:-1]) from isPal with argument', s) //test statement
##        return s[0] == s[-1] and isPal(s[1:-1])
##        
##    return isPal(tochars(s))
##
##
## x = user input //prompt user for input
##
## while x != '': //while x is not a blank character
##    toChars(x) //run x through the toChars function
##    isPal(x) //run x through the isPal function
##    if isPalindrome(x): //checks if input is a palindrome
##        print(x, 'is a palindrome')
##    else:
##        print(x, 'is not a palindrome')
##
##    x = userinput:  ') //reprompt users for string.
##    
##print('Finished!')

def isPalindrome(s):
    '''checks whether a string s is a palindrome'''
    if type(s) == str:
        print('About to return True from isPalindrome as input is string')
        return True
    else:
        print('About to return False from isPalindrome as input is not string')
        return False

def toChars(s):
    '''Converts a string to lowercase and removes non-letters'''
    s = s.lower()
    letterstring = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letterstring += c
    print ('About to return letterstring value from toChars')
    return letterstring

def isPal(s):
    '''checks whether string s is a palindrome assumes s is string with only lowercase letters and no non-letters
    returns True if s is a Palindrome; returns False otherwise. Recrusive function '''
    print ('isPal function called with argument', x)
    if len(s) <= 1:
        print ('About to return True from isPal for the base case')
        return True
    else:
        print('About to return result s[0] == s[-1] and isPal(s[1:-1]) from isPal with argument', s)
        return s[0] == s[-1] and isPal(s[1:-1])
        
    return isPal(tochars(s))


x = input('Enter a string (empty string to exit):  ')

while x != '':
    toChars(x)
    isPalindrome(x)
    if isPal(x):
        print(x, 'is a palindrome')
    else:
        print(x, 'is not a palindrome')

    x = input('Enter a string (empty string to exit):  ')
    
print('Finished!')
