import math

length = None


length = int (input('Enter the value you wish to use: '))
if length <= 0:
    print ("Length must be >=0. Please try again")
else:
    square_area = length ** 2
    print ('The area of a square with side' , length , 'is: ' , square_area)
    cube_volume = length ** 3
    print ('The volume of a cube with radius', length , ' is: ' , cube_volume)
    circle_area = math.pi * (length ** 2)
    print ('The area of a circle with radius', length , ' is: ' , circle_area)
    sphere_volume = 4/3 * math.pi * (length ** 3)
    print ('The volume of a sphere with radius', length , ' is: ' , sphere_volume)
    cylinder_volume = math.pi * (length ** 2) * length
    print ('The volume of a cylinder with height', length , ' is: ' , cylinder_volume)
