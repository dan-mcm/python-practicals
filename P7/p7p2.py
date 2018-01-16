year = int (input ( 'Please insert a year: '))

#test condition to verify input worked
print ('You have entered: ' ,  year)

if (year %4 != 0):
    print('it is a common year');
elif (year %100 != 0):
    print('it is a leap year');
elif (year %400 != 0):
    print('it is a common year');
else:
    print('it is a leap year');
