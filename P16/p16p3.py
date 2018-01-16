# Psuedocode
#x = user input //take users input (question does not state for repeated user input...)
#
#factors = [i for i in range(1,x+1) if x % i == 0] //sets variable factors to value of i where i falls in the range of 1 up to the value of user input+1 where the user input is divisible by the value of i
#if sum(factors) == 2*x: //if sum of the factors is equal to twice the user input then print factors.
#    print (factors)
#else:
#    print ('Number has no proper factors.') //otherwise notify user number inserted has no proper factors
#


x = int(input('Please insert positive int: '))

factors = [i for i in range(1,x+1) if x % i == 0]
if sum(factors) == 2*x:
    print (factors)
else:
    print ('Number has no proper factors.')
    
