a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0

while(True):
    x = int (input('Enter the integer you wish to use: '))
    if x == 0:
        print('Number is equal to 0');
        a += 1
    elif x > 0 and x <= 20:
        print('Number is greater than 0 and less than or equal to 20');
        b += 1
    elif x > 20 and x <= 40:
        print('Number is greater than 20 and less than or equal to 40');
        c += 1
    elif x > 40 and x <= 60:
        print('Number is greater than 40 and less than or equal to 60');
        d += 1
    elif x > 60 and x <= 80:
        print('Number is greater than 60 and less than or equal to 80');
        e += 1
    elif x > 80 and x <= 100:
        print('Number is greater than 80 and less than or equal to 100');
        f += 1
    elif x > 100:
        print('Number is greater than 100');
        g += 1
    else:
        print ('Number of times 0 was entered =', a);
        print ('Number of times between 0-20 was entered =', b);
        print ('Number of times between 21-40 was entered =', c);
        print ('Number of times between 41-60 was entered =', d);
        print ('Number of times berween 61-80 was entered =', e);
        print ('Number of times between 81-100 was entered =', f);
        print ('Number of times 100+ was entered =', g);
        print ('Negative Integer Detected - Program End');
        break
