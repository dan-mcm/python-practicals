#Psuedocode
#x = user input //takes user input
#y = 0.01 //tolerance variable
#step = y **2 //change in figure used for value y
#
#def function(a,b): //defines function that takes 2 arguments
#
#    root = 0.0 //sets defualt root to 0.0
#    z = 0
#    if (x<0): //if input is negative then return error message and exit loop (return None)
#        print('Negative int detected - Program End!')
#        return
#    else:
#        while abs(x - root **2) >= y and root **2 <= x: //while value of input - root squared is greater than loerance and less than user input
#            root += step //increment root by step
#            z +=1 //increment z value by 1
#            if z % 10000 == 0: //if modulus 10000 is zero (where 10000 is our number of guesses at the root...)
#                print('Still running. Number of guesses:', z) //print still running guesses
#        print ('Number of guesses', z) //print number of guesses
#        if abs(x - root ** 2) < y: //if absolute value of input - root squared is less than tolerance value
#            print('The approximate square root of', x, 'is', root) //the approx square root of input is root
#        else:
#            print('Failed to find the square root', x) //else print failed to find square root
#    print('Finished!') //print finished at end of program
#
#
#function(x, y) //run function with parameters x (user input) and y (tolerance value defined in program)

x = int(input('Insert number to check square root: '))
y = 0.01
step = y **2

def function(a,b):

    root = 0.0
    z = 0
    if (x<0):
        print('Negative int detected - Program End!')
        return
    else:
        while abs(x - root **2) >= y and root **2 <= x:
            root += step
            z +=1
            if z % 10000 == 0:
                print('Still running. Number of guesses:', z)
        print ('Number of guesses', z)
        if abs(x - root ** 2) < y:
            print('The approximate square root of', x, 'is', root)
        else:
            print('Failed to find the square root', x)
    print('Finished!')


function(x, y)
