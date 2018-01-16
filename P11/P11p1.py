#Psuedocode
#number = user input //takes user input
#fact = 0; //declares initial factorial variable
#
#if number < 0: //set if number is negative print error message
#    print('Error: Number entered was less than 0.')
#else:
#    fact = 1
#    for i in range (1, number + 1): //else  fact = fact * i
#         fact *= i
#
#    print('Factorial of', number, 'is',  fact) //prints factorial number and value
#
#print ('Finished!') //prints finished to indicate end of program




number = int(input('Please insert number: '))
fact = 0;

if number < 0:
    print('Error: Number entered was less than 0.')
else:
    fact = 1
    for i in range (1, number + 1):
         fact *= i

    print('Factorial of', number, 'is',  fact)

print ('Finished!')
