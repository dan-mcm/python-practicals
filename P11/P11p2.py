#Psuedocode
#limit = user input //takes input from user
#f0 = 0 //holds first value of fibonacci series (will change each time loop runs)
#f1 = 1 //holds second value of fibonacci series (will change each time loop runs)
#
#if limit <=0: //if user input is less than 0 print error message
#    print ('Error: Number must be greater than 0')
#elif limit == 1: //if user input is 1, then print series = f0
#    print ('Series is:', f0)
#elif limit == 2: //if user input is 2, then print series = f0, f1
#    print ('Series is: ', f0,  ',' , f1, sep = "")
#else:
#    print('Series is: ', f0,  ',', f1, sep = "", end = "") //otherwise print series if f0, f1
#
#a = f0 //assigns f0 to a
#b = f1 //assigns f1 to b
#
#i = 2 //sets i to 2
#
#while i < limit: //while limit is greater than 2 (conditions 1, 2 handled above)
#    fib = b + a //fibonacci sequence is sum of b and a
#    print(',', fib, end = "") //print fibonacci series
#
#    a = b //sets value of a to b (progressing through the fib series)
#    b = fib //sets value of b to fib
#    i += 1 //increments i
#
#print()
#
#print('Finished!')


limit = int(input('Enter Number of Terms Wish to Calculate: '))
f0 = 0
f1 = 1

if limit <=0:
    print ('Error: Number must be greater than 0')
elif limit == 1:
    print ('Series is:', f0)
elif limit == 2:
    print ('Series is: ', f0,  ',' , f1, sep = "")
else:
    print('Series is: ', f0,  ',', f1, sep = "", end = "")

a = f0
b = f1

i = 2

while i < limit:
    fib = b + a
    print(',', fib, end = "")

    a = b
    b = fib
    i += 1

print()

print('Finished!')
