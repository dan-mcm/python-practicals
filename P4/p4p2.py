import math

length = None

#area of a square
length = int (input('Enter the side value you wish to use to calculate the area of a square: '))
square_area = length ** 2
print ('The area of a square with side' , length , 'is: ' , square_area)


#volume of a cube
length = int (input('Enter the radius you wish to use to calculate the volume of a cube: '))
cube_volume = length ** 3
print ('The volume of a cube with radius', length , ' is: ' , cube_volume)

#area of a circble
length = int (input('Enter the radius you wish to use to calculate the area of a circle: '))
circle_area = math.pi * (length ** 2)
print ('The area of a circle with radius', length , ' is: ' , circle_area)

#volume of a sphere
length = int (input('Enter the radius you wish to use to calculate the volume of a sphere: '))
sphere_volume = 4/3 * math.pi * (length ** 3)
print ('The volume of a sphere with radius', length , ' is: ' , sphere_volume)

#volume of a cylinder
length = int (input('Enter the height you wish to use to calculate the volumeof a cylinder: '))
cylinder_volume = math.pi * (length ** 2) * length
print ('The volume of a cylinder with height', length , ' is: ' , cylinder_volume)






