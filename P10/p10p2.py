# Psuedocode
#
# x = user input
# if x > 0: //this will allow us account for positive ints - else statement at end of loop will account for negative input
#
#    for square_root in range (abs(x) + 1): //runs from 0 up to absolute value of x+1. (allows renumerative iteration)
#        if square_root **2 >= abs(x):  //if square root squared is greater than the absolute value of x break loop.
#           break //kick program out of loop
#
#   if square_root **2 == abs(x): //if the square root value ^2 is equal to the absolute value of x
#        print('Square root of', x, 'is', square_root) //print the squared root of variable is 'value'
#   else:
#              print(x, 'is not a perfect square.') //otherwise print the inputted value is not a perfect square.
#              
#  else:
#   print('negative int deteceted - program end') //print alert that negative int was enetered and close program
#


while(True):
    
    x = int(input("Please insert Int:"))
    if x > 0 or  x<0:

        for cube_root in range (abs(x) + 1): 
            if cube_root **3 >= abs(x):  
                break

        if cube_root **3 == abs(x): 
            if x < 0: 
                cube_root = -cube_root 
            print('Cubed root of', x, 'is', cube_root) 
        else:
                  print(x, 'is not a perfect cubed root.') 
    else:
        print('0 detected - program end') 
        break; 
