# Psuedocode
#
#while(True): //creates an infinite loop
#    x = userinput
#   v1 = 2 //stores variable 1
#    v2 = 0 //stores variable 2
#
#   def funct(x): //define your function to undertake the calculations
#        """Function that returns the value of its argument put through equation in question
#        Uses a recursive definition
#        """
#        if x == 1: //as per formulae if x is 1 print out value of 2
#            print("Value of 1 through function is = ", v1)
#                  
#        else: //if x is more than 1 then do the following
#            print('Series is: ', v1, sep = "", end = "") //prints out innitial value of series...
#            a = v1 //assigns value of a
#            b = v2 //assigns value of b
#
#            for i in range (2,x+1): //while within the range 2 to user input +1
#                res = a + (a-1) //variable result will equal to calculation (as interprted from formulae)
#                print ('\n current value of a is' ,a, 'current value of b is',b,'next value in sequence should be a + (a-1):', res) //print out the test statement
#                print(',',res, end ="") //print results out for series.
#                a = b //reassign var a
#                b = res //reassign var b
#        print()
#
#    if x > 0:  //if user input is positive
#            funct(x) //run function
#    else:
#            print('Error - Negative Int Detected - Program End') //otherwise break from the loop.
#            break
#


while(True):
    x = int(input('Please insert your input: '))
    v1 = 2
    v2 = 0

    def funct(x):
        """Function that returns the value of its argument put through equation in question
        Uses a recursive definition
        """
        if x == 1:
            print("Value of 1 through function is = ", v1)
                  
        else:
            print('Series is: ', v1, sep = "", end = "")
            a = v1
            b = v2

            for i in range (2,x+1):
                res = a + (a-1)
                print ('\n current value of a is' ,a, 'current value of b is',b,'next value in sequence should be a + (a-1):', res)
                print(',',res, end ="")
                a = b
                b = res
        print()

    if x > 0:
            funct(x)
    else:
            print('Error - Negative Int Detected - Program End')
            break

    #comment correct item: y=(n+function(n-1)). return y.


