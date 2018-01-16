year = int ( input ( 'Please insert a year:' ) )

print ('You have entered: ' ,  year)

if year >= 0:
    if ( year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
        print (year , 'is a leap year.')
    else:
        print (year , 'is not a leap year.')
else:
    print ('Year value must be above 0.')

print ('Program end.')
