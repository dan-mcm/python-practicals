import math

length = 095563.62
radius = length/2

square_area = length ** 2
cube_volume = length ** 3
circle_area = math.pi * (radius ** 2)
sphere_volume = 4/3 * math.pi * (radius ** 3)
cylinder_volume = math.pi * (radius **2) * length

print ('The Square Area is: ' , square_area)
print ('The Cube Volume is: ' , cube_volume)
print ('The Circle Area is: ' , circle_area)
print ('The Sphere Volume is: ' , sphere_volume)
print ('The Cylinder Volume is: ' , cylinder_volume)
