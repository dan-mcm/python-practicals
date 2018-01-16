x = int (input('Enter the integer you wish to use: '))

if x == 0:
    print('Number is equal to 0');
elif x > 0 and x <= 20:
    print('Number is greater than 0 and less than or equal to 20');
elif x > 20 and x <= 40:
    print('Number is greater than 20 and less than or equal to 40');
elif x > 40 and x <= 60:
    print('Number is greater than 40 and less than or equal to 60');
elif x > 60 and x <= 80:
    print('Number is greater than 60 and less than or equal to 80');
elif x > 80 and x <= 100:
    print('Number is greater than 80 and less than or equal to 100');
elif x < 0:
    print('Number is less than 0');
else:
    print('Number is greater than 100');
    
