x = int (input('Please enter first int: '))
y = int (input('Please enter second int:'))
z = int (input('Please enter third int:'))

if (x%2 == 1 or y%2 == 1 or z%2 == 1):
    if (x>y and x>z):
        print(x, 'is the largest odd number');
    elif (y>x and z>x):
        print(y, 'is the largest odd number');
    else:
        print(z, ' is the largest odd number');

if(x%2 == 0 and y%2 == 0 and z%2 == 0):
    print('All numbers are positive');
