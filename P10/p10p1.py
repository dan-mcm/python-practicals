# Psuedocode:
#
# x = //user input
# if x > 0: //this will allow us account for positive ints - else statement at end of loop will account for negative input
#
#  for square_root in range (abs(x) + 1): //runs from 0 up to absolute value of x+1. (allows exhaustive emuneration)
#  if square_root **2 >= abs(x): // if square root squared is greater than the absolute value of x break loop.
#  break //kicks program out of loop
#
 #   if square_root **2 == abs(x): #if the square root value ^2 is equal to the absolute value of x
 #       print('Square root of', x, 'is', square_root) //print the squared root of variable is 'value'
 #   else:
 #             print(x, 'is not a perfect square.') //otherwise print the inputted value is not a perfect square.
 #             
#else:
#    print('negative int deteceted - program end') //print alert that negative int was enetered and close program




x = int(input("Please insert Int:"))
if x > 0:
    
    for square_root in range (abs(x) + 1): 
        if square_root **2 >= abs(x):  
            break

    if square_root **2 == abs(x): 
        print('Square root of', x, 'is', square_root) 
    else:
              print(x, 'is not a perfect square.')
              
else:
    print('negative int deteceted - program end')
