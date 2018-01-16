# a = 'a' //define variables for various string letters you wish to test for/
# e = 'e'
# i = 'i'
# o = 'o'
# u = 'u'
#
# x = user input
#
# while(x != ''): //while the string is NOT empty (i.e. there is user input
#
#    a1 = 0 //definine counters for each time an a e i o u is entered
#    e1 = 0
#    i1 = 0
#    o1 = 0
#    u1 = 0
#    
#    y = len(x) //define y as the length of the user input
#    
#    for f in range (0, abs(y)): //for value in the range 0 to the absolute value of the strings length
#        if a in x[f]:  //if the character a is in the string range (repeat for each string)
#            a1 += 1 //increment the counter a1 by 1 (a1 = a1 + 1)
#        if e in x[f]:
#            e1 += 1
#        if i in x[f]:
#            i1 += 1
#        if o in x[f]:
#            o1 += 1
#        if u in x[f]:
#            u1 += 1
#   
#    else:
#     print ('Number of times a was entered =', a1); //this prints the number of times each vowel was entered
#     print ('Number of times e was entered =', e1);
#     print ('Number of times i was entered =', i1);
#     print ('Number of times o was entered =', o1);
#     print ('Number of times u was entered =', u1);
#
#       x = str (input('Enter the String you wish to use: ')) //reprompt user for input (included in while loop to allow user to input multiple times)
#   
#    else: //if the string is empty then tell user and end program

#    print('Empty string entered - Program end');

a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u'

x = str (input('Enter the String you wish to use: '))

while(x != ''):

    a1 = 0
    e1 = 0
    i1 = 0
    o1 = 0
    u1 = 0
    
    y = len(x)
    
    for f in range (0, abs(y)):
        if a in x[f]:
            a1 += 1
        if e in x[f]:
            e1 += 1
        if i in x[f]:
            i1 += 1
        if o in x[f]:
            o1 += 1
        if u in x[f]:
            u1 += 1
    
    else:
        print ('Number of times a was entered =', a1);
        print ('Number of times e was entered =', e1);
        print ('Number of times i was entered =', i1);
        print ('Number of times o was entered =', o1);
        print ('Number of times u was entered =', u1);

        x = str (input('Enter the String you wish to use: '))
    
else:
    print('Empty string entered - Program end');


