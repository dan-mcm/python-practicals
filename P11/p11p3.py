#Psuedocode
#
#limit = user input //takes user input
#f0 = 0 //assigns fibonnaci values to variables
#f1 = 1
#
#while(True): // allows infinite loop - usercan re-enter integer values at end of loop
#    if limit <=0: // if limit is less than or equal to 0 print error and break from loop.
#        print ('Error: Negative Int!!! Program Terminate')
#        break
#    elif limit == 1:
#        print ('Series is:', f0) //declare scenario if input is 1
#    elif limit == 2:
#        print ('Series is: ', f0,  ',' , f1, sep = "") //declare scenario if input is 2
#    else:
#        print('Series is: ', f0,  ',', f1, sep = "", end = "") //declare series of variables
#
#    a = f0 //assigns f0 and f1 to a and b
#    b = f1
#
#    for i in range (2,limit): //for loop instead of while as per brief
#        fib = b + a
#        print(',', fib, end = "")
#
#        a = b //a value is assign value of b (next number in fib sequence)
#        b = fib
#
#    print()
#
#    limit = int(input('Enter Number of Terms Wish to Calculate: ')) //allows user to reinput number

limit = int(input('Enter Number of Terms Wish to Calculate: '))
f0 = 0
f1 = 1

while(True):
    if limit <=0:
        print ('Error: Negative Int!!! Program Terminate')
        break
    elif limit == 1:
        print ('Series is:', f0)
    elif limit == 2:
        print ('Series is: ', f0,  ',' , f1, sep = "")
    else:
        print('Series is: ', f0,  ',', f1, sep = "", end = "")

    a = f0
    b = f1

    for i in range (2,limit):
        fib = b + a
        print(',', fib, end = "")

        a = b
        b = fib

    print()

    limit = int(input('Enter Number of Terms Wish to Calculate: '))
