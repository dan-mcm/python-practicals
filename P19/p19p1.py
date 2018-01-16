##Psuedocode
##
##u = user Base 10 number input
##v = user Base to convert to input
##print('Converting', u, 'to Base', v) //test statement to ensure details are correct
##
##def conversion(x,y): //define function
##    '''function that converts base 10 numbers to base 2,8 and partly 16. Also condition to attempt
##    other base estimates'''
##    a = str ('') //initialise a as empty string
##    if y == 2: //if base case 2 is inserted do the following - prints an additional Binary string statement
##        print('You selected Binary conversion!')
##        while x > 0:
##            a += str(x%y)
##            x = x//y      
##        print('Answer is: ', a[::-1]) # .reverse() does not work on strings - implemented this solution (extended slice syntax). works fine for bases up to 9, afterwards can cause issues - espeically if letters get involved. technique sourced from stackoverflow
##    elif y == 8: //sets condition for octals - prints additional Octal string statement
##        print('You selected Octal conversion!')
##        while x > 0:
##            a += str(x%y)
##            x = x//y
##        print('Answer is: ', a[::-1])
##    elif y == 16: //sets condition for octals - prints additional Octal string statement
##        print('You selected Hexadecimal conversion! Note:  does not convert end number correctly to letter if remainder is between 10-15')
##        while x > 0: //this while loop has additional checks for letters - only half works as due to extend slice synax used it wont successfully read numbers 10-15 and translate as it reads them as 01 11 21 31 41 51
##            if x%16==10:
##                a += 'A'
##            elif x%16==11:
##                a +='B'
##            elif x%16==12:
##                a +='C'
##            elif x%16==13:
##                a +='D'
##            elif x%16==14:
##                a +='E'
##            elif x%16==11:
##                a +='F'
##            else:
##                a+= str(x%y)
##            x = x//y
##        print('Answer is: ', a[::-1])
##            
##    else: //this is a catch all in the event the input is not a standard 2,8,16 - it gives an estimate of an estimation provided string does not contain numbers.
##        print('I am unfamiliar with that base... but here is an estimate...')
##        while x > 0:
##            a+= str(x%y)
##            x = x//y
##        print('Answer is: ', a[::-1])
##
##conversion(u,v) //runs function with user input as values.


u = int(input('Please insert Base 10 Number: '))
v = int(input('Please insert Base number you wish to translate number to (2,8.16)'))
print('Converting', u, 'to Base', v)

def conversion(x,y):
    '''function that converts base 10 numbers to base 2,8 and partly 16. Also condition to attempt
    other base estimates'''
    a = str ('')
    if y == 2:
        print('You selected Binary conversion!')
        while x > 0:
            a += str(x%y)
            x = x//y      
        print('Answer is: ', a[::-1]) # .reverse() does not work on strings - implemented this solution (extended slice syntax)
    elif y == 8:
        print('You selected Octal conversion!')
        while x > 0:
            a += str(x%y)
            x = x//y
        print('Answer is: ', a[::-1])
    elif y == 16:
        print('You selected Hexadecimal conversion! Note:  does not convert end number correctly to letter if remainder is between 10-15')
        while x > 0:
            if x%16==10:
                a += 'A'
            elif x%16==11:
                a +='B'
            elif x%16==12:
                a +='C'
            elif x%16==13:
                a +='D'
            elif x%16==14:
                a +='E'
            elif x%16==11:
                a +='F'
            else:
                a+= str(x%y)
            x = x//y
        print('Answer is: ', a[::-1])
            
    else:
        print('I am unfamiliar with that base... but here is an estimate...')
        while x > 0:
            a+= str(x%y)
            x = x//y
        print('Answer is: ', a[::-1])

conversion(u,v)
