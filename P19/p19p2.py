##Psuedocode
##
##u = user input number //takes users number
##v = user base number //takes base of number user has inputted
##
##def  conversion(x,y): //define sfunction
##    '''function converts inserted number to base 10'''
##    decimal = 0 //declaring decimal value
##    x=str(x) //convert x to string so as to set range of for loop to length of string.
##    for i in range (len(x)):
##        decimal += int(x[-(i+1)]) * (y**i) //converts x back to int and takes the index of -(i+1) and multiplies it by the base number times i.
##    print(decimal) //prints output
##    return decimal //returns decimal.
##
##conversion(u,v) //run function with user input as variables
##

u = int(input('Please insert your number: '))
v = int(input('Please insert Base number - we will translate your result to Base 10: '))

def  conversion(x,y):
    '''function converts inserted number to base 10 - does not work for base greater than 10'''
    decimal = 0
    x=str(x)
    for i in range (len(x)):
        decimal += int(x[-(i+1)]) * (y**i)
    print(decimal)
    return decimal

conversion(u,v)
