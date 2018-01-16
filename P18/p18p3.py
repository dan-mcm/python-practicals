##x = str(input('Please insert string:  ')) //casts user input as string value (extra security)
##
##def codeDetect(a): //setup function
##
##    counter = 0 //set counter to 0
##    i = 0 //set i to 0
##    for i in range (i,len(a)-2): //for i in the range i (start of string) to length of the string, -2 is used so it doenst break if 'co' at end of string
##        if a[i:i+2] == 'co' and a[i+2].isalpha() and a[i+3] == 'e'://if i is = co and is alphabetic and the letter alpha it is e...
##            counter += 1 //increment counter
##    print ('code occurs', counter, 'times')
##
##
##codeDetect(x)


x = str(input('Please insert string:  '))

def codeDetect(a):
    '''function that prints out number of times co*e appears where * is alphabetic character'''
    counter = 0
    i = 0
    for i in range (i,len(a)-2):
        if a[i:i+2] == 'co' and a[i+2].isalpha() and a[i+3] == 'e':
            counter += 1
    print ('code occurs', counter, 'times')


codeDetect(x)

