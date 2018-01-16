# Psuedocode
#
#def findDivisors(num1,num2): //define function that takes 2 argumets
 #    divisors = () //define divisors
#    for i in range (1, min(num1,num2)+1):
#        if num1 % i == 0 and num2 % i == 0: //for loop  will check divisors of both numbers and add them to divisors.
#            divisors += (i,)
#    return divisors //returns divisors
#
#x = user input // takes user input for x value
#y = user input //  takes user input for y value
#
#if x <= 0 or y <= 0:
#    print('Numbers should be > 0.') //check to ensure numbers entered are positive
#else:
#    divisors = findDivisors(x,y) //assigns divisors the values of the user input
#    print('The common divisors of', x, 'and', y, 'are', divisors) //prints out divisors of the user input.
#

def findDivisors(num1,num2):
    divisors = ()
    for i in range (1, min(num1,num2)+1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i,)
    return divisors

x = int(input('Please insert x value: '))
y = int(input('Please insert y value:'))

if x <= 0 or y <= 0:
    print('Numbers should be > 0.')
else:
    divisors = findDivisors(x,y)
    print('The common divisors of', x, 'and', y, 'are', divisors)


