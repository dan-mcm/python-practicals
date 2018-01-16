# Psuedocode
#
# x = str(input('Please insert cat and dog strings:  ')) //take user input
#
# print('Number of occurances of cat: ',  x.count('cat')) //test statement for nubme of cat detected
# print('Number of occurances of dog:  ', x.count('dog')) //test statement for number of dog detected
#
# if x.count('cat') == x.count('dog'): //check if the number in count is same for both cat and dog
#     print('Number of occurances of cat and dog are the same!')
# else: //runs print statement if number of occurances is not the same
#     print('Number of occurances of cat and dog are not the same!')
#


x = str(input('Please insert cat and dog strings:  '))

print('Number of occurances of cat: ',  x.count('cat'))
print('Number of occurances of dog:  ', x.count('dog'))

if x.count('cat') == x.count('dog'):
    print('Number of occurances of cat and dog are the same!')
else:
    print('Number of occurances of cat and dog are not the same!')
