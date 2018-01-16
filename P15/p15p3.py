# Psuedocode
#while(True):  //creates infintie loop allowing user to input multiple times.
#    x = user input
#    v1 = 13 //variable for first in series
#    v2 = 8 //variable for second in series
#    
#
#    def funct(x): //declares function
#        """Function that returns the value of its argument put through equation in question
#        Uses a recursive definition
#        """
#        if x == 1: //if user intput is one it prints out the value of the 0 term in series which is 13
#            print("Series is: ", v1)
#            
#        elif x == 2: //if user input is two it prints out the value of the 1 term in series which is 8
#            print("Series is = ", v1, ',', v2)
#                  
#        else: //for all other cases...
#            print('Series is: ', v1, ',', v2, sep = "", end = "") //prints out first 2 in series....
#            a = v1 //assigns a and b
#            b = v2
#
#            for i in range (2,x+1): //between 2 and input+1
#                res = (a-2) + 13 * (a-1) //formulae as interpreted from brief...
#                print ('\n current value of a is' ,a, 'current value of b is',b,'next value in sequence should be (a-2) + 13 * (a-1):', res) //test statement
#                print(',',res, end ="") //prints out extra values in series
#                a = b //reassigns a value
#                b = res /reassigns b value
#        print()
#
#    if x >= 0:  //if x is postiive run function
#            funct(x)
#    else: //otherwise print error and break from infinite loop
#            print('Error - Negative Int Detected - Program End')
#            break
#
#
#

while(True):
    x = int(input('Please insert your input: '))
    v1 = 13
    v2 = 8

    def funct(x):
        """Function that returns the value of its argument put through equation in question
        Uses a recursive definition
        """
        if x == 1: 
            print("Series is: ", v1)
            
        elif x == 2:
            print("Series is = ", v1, ',', v2)
                  
        else:
            print('Series is: ', v1, ',', v2, sep = "", end = "")
            a = v1
            b = v2

            for i in range (2,x+1):
                res = (a-2) + 13 * (a-1)
                print ('\n current value of a is' ,a, 'current value of b is',b,'next value in sequence should be (a-2) + 13 * (a-1):', res)
                print(',',res, end ="")
                a = b
                b = res
        print()

    if x >= 0:
            funct(x)
    else:
            print('Error - Negative Int Detected - Program End')
            break
