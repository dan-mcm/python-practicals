# Psuedocode
#
#def findDivisors(num1): //define function that takes 1 argument
#    divisors = (1,num1) //divisors initialised with 1,and x user input values.
#    for i in range (2, (num1+1)//2): //modified range between 2 and half of the number
#        if num1 % i == 0: //for loop  will check divisors of both numbers and add them to divisors.
#            divisors += (i,)
#    return divisors //returns divisors
#
#x = user input // takes user input for x value
#
#if x <= 0:
#    print('Numbers should be > 0.') //check to ensure numbers entered are positive
#else:
#    divisors = findDivisors(x) //assigns divisors the values of the user input
#    print('The common divisors of', x, 'are', divisors) //prints out divisors of the user input.
#

def findDivisors(num1):
    ''' program to get the common divisors of two positive integers supplied
    '''
    divisors = (1,num1)
    for i in range (2, (num1+1)//2):
        if num1 % i == 0:
            divisors += (i,)
    return divisors

x = int(input('Please insert x value: '))

if x <= 0:
    print('Numbers should be > 0.')
else:
    divisors = findDivisors(x)
    print('The common divisors of', x, 'are', divisors)
