# Psuedocode
# for number in range (2,20)
#   for i in range (2,number):
#       if number has no remainder:
#           print number equal to number 1 by number 2
#           break out of the loop
#       else
#           if number has no remainder - print its a prime number
#
#   print finished at end of program.
#



for number in range (2,20):
    for i in range (2,number):
        if number %i == 0:
            print(number, 'equals', i, '*', number//i)
            break
    else:
        print(number, 'is a prime number')
        
print ('Finished!')
