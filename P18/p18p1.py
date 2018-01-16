# Psuedocode
##
##def isPalindrome(s): //creates function to check if input is a string
##    '''checks whether a string s is a palindrome'''
##    if type(s) == str: //if input is a string return true otherwise return false
##        return True
##    else:
##        return False
##
##def toChars(s): //converts string to lowercase and removes non-letters
##    '''Converts a string to lowercase and removes non-letters'''
##    s = s.lower() //sets chars in s to lowercase
##    letterstring = ''
##    for c in s:
##        if c in 'abcdefghijklmnopqrstuvwxyz':
##            letterstring += c 
##    return letterstring
##
##def isPal(s):
##    ''''checks whether string s is a palindrome assumes s is string with only lowercase letters and no non-letters
##    returns True if s is a Palindrome; returns False otherwise. Recrusive function '''
##    length = len(s) //gets length of  string inputted
##    limit = length//2  //get integer divisible of length divide by 2
##    sem = True //semaphore value set to true
##    counter = 0 // acts as limited counter and pos number representation simultaneously
##    negnum = -1 //sets value for end number of strings
##
##    while counter < limit: //while counter is less than limit
##        if (s[counter] !=  s[negnum]): //if the edge ases are not equal return semaphore value False
##            sem = False
##            break
##        counter += 1  //otherwise increment positive checker and decrement negative chereker
##        negnum -= 1
##
##    return sem
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
    '''checks whether a string s is a string'''
    if type(s) == str:
        return True
    else:
        return False

def toChars(s):
    '''Converts a string to lowercase and removes non-letters'''
    s = s.lower()
    letterstring = ''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            letterstring += c
    return letterstring

def isPal(s):
    '''checks whether string s is a palindrome assumes s is string with only lowercase letters and no non-letters
    returns True if s is a Palindrome; returns False otherwise. Recrusive function '''
    length = len(s)
    limit = length//2
    sem = True
    counter = 0 #acts as pos number simultaneously
    negnum = -1

    while counter < limit:
        if (s[counter] !=  s[negnum]):
            sem = False
            break
        counter += 1
        negnum -= 1

    return sem
        
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

