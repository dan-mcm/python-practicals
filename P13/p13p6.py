#Psuedocode
#Num = user input //detects user input
#
#def fact(x): //defines function
#    """Function that returns the factorial of its argument
#    Assumes that its argument is a non-negative integer
#    Uses a recursive definition
#    """
#    if x < 0:
#        print("Error - Negative Int Detected - Program End") //prints error if input is negative
#        
#    elif x == 0:
#        return 1
#    
#    else:
#        print(x,  'factorial is equal to', x ,'*', 'fact(',x- 1,')') //statement prints recursive factorials as evidence of recursive operation
#        return x * fact(x - 1)  //returns factorial value
#
# print('Result of', Num, 'factorial is', fact(Num)) //prints factorial value



Num = int(input('Please insert your input: '))

def fact(x):
    """Function that returns the factorial of its argument
    Assumes that its argument is a non-negative integer
    Uses a recursive definition
    """
    if x < 0:
        print("Error - Negative Int Detected - Program End")
        
    elif x == 0:
        return 1
    
    else:
        print(x,  'factorial is equal to', x ,'*', 'fact(',x- 1,')')
        return x * fact(x - 1) 

print('Result of', Num, 'factorial is', fact(Num))
