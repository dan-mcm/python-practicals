# Psuedocode
#
# x = user input
# fo = 0 //for series 1 case
# f1 = 1 //for series 2 case
#
# 
# declare function //funtion checks user input...
# if x  <=0  // if user input is negative...
#  terminate program
#
# if x  == 1 //if user input is 1...
# print fo
#
# if x == 2 //if user input is 2...
# print fo,f1
#
# else //if user input is more than 2...
# print fo,f1  // first 2 terms in series, include rest using below...
#
# a = f0
# b = f1
#
# for i in the range (2,x+1) //for the values between 2 and userinput +1
# print a test to see the values actively changing each time.
# print the next term
# reassign a = b
# make b = latest in the fib series.
#
# run function with user input as argument.
#

x = int(input('Insert argument: '))
f0 = 0
f1 = 1

def function(a):
    '''
    Function is designed to check user input - if 0 terminate, if 1 return fo, if  2 return fo f1,
    if more than 2 add extra based on addition of the fib variable

    '''
    
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

    for i in range (2,x+1):
        fib = b + a
        print ('\n current value of a is' ,a, 'current value of b is',b,'next value in sequence should be (a+b):',fib)
        print(',', fib, end = "") #this demonstrates the recursion elements in practice
       
        a = b
        b = fib

    print()

function(x)
