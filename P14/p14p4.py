# Psuedocode
# for number in range (2,20)
#   let the variable x = 1 // this will act as a semaphore
#   for i in range (2,number):
#       if number has no remainder:
#           print number equal to number 1 by number 2
#           let x = 0 //switch semaphore state - forces program to run though entire range first.
#       else
#           if semaphore value is 1...
#           print its a prime number
#
#   print finished at end of program.
#

for number in range (2,20):
    x = 1
    for i in range (2,number):
        if number %i == 0:
            print(number, 'equals', i, '*', number//i)
            x = 0
    else:
        if  x == 1:
            print(number, 'is a prime number')
        
print ('Finished!')
