# Psuedocode
#
# x = user input //take user input
# def printCount(a):
#   print('Number of occurances of  the word "code" in the string is: ',  x.count('code')) //prints number of occurances of code in string
# printCount(x) //print function


x = str(input('Please insert string:  '))

def printCount(a):
    '''function that prints out count of word code in series'''
    print('Number of occurances of  the word "code" in the string is: ',  x.count('code'))

printCount(x)
