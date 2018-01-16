#Psuedocode
#x = user input //takes user input
#f0 = 0 
#f1 = 1
#
#def function(a): //defines function
#    if x <=0: //if input negative print error message and return None
#        print ('Error: Negative Int!!! Program Terminate')
#        return
#    elif x == 1:
#        print ('Series is:', f0) //if input 1 print f0
#        
#    elif x == 2:
#        print ('Series is: ', f0,  ',' , f1, sep = "") //if input 2 print f0, f1
#    else:
#        print('Series is: ', f0,  ',', f1, sep = "", end = "") //else print values
#
#    a = f0
#    b = f1
#
#    for i in range (2,x): //calculates fibonacci series
#        fib = b + a
#        print(',', fib, end = "")
#
#        a = b
#        b = fib
#
#    print()
#
#function(x) //runs function with value x

x = int(input('Insert argument: '))
f0 = 0
f1 = 1

def function(a):
    if x <=0:
        print ('Error: Negative Int!!! Program Terminate')
        return
    elif x == 1:
        print ('Series is:', f0)
        
    elif x == 2:
        print ('Series is: ', f0,  ',' , f1, sep = "")
    else:
        print('Series is: ', f0,  ',', f1, sep = "", end = "")

    a = f0
    b = f1

    for i in range (2,x):
        fib = b + a
        print(',', fib, end = "")

        a = b
        b = fib

    print()

function(x)
