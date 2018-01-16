# Psuedocode
# def f(x, y, z, t, u, v): //passes variables through function
#    """Function that adds 1 to its argument and prints it out"""
#    print('In function f:')
#    x += 1
#    y = 1
#    t += 1
#    u += 1
#    v += 1
#    print('x is', x)
#    print('y is', y)
#    print('z is', z)
#    print('t is', t)
#    print('u is', u)
#    print('v is', v)
#    return t //function returns t value

# x, y, z, t, u, v = 5, 10, 15, 6, 11, 16 //sets variables

# print('Before function f:') //prints variable values before going through function
# print('x is', x)
# print('y is', y)
# print('z is', z)
# print('t is', t)
# print('u is', u)
# print('v is', v)

# t = f(x, y, z, t, u, v)

# print('After function f:') //prints variable values after going through function
# print('x is', x)
# print('y is', y)
# print('z is', z)
# print('t is', t)
# print('u is', u)
# print('v is', v)





# Program to illustrate scoping in Python
def f(x, y, z, t, u, v):
    """Function that adds 1 to its argument and prints it out"""
    print('In function f:')
    x += 1
    y = 1
    t += 1
    u += 1
    v += 1
    print('x is', x)
    print('y is', y)
    print('z is', z)
    print('t is', t)
    print('u is', u)
    print('v is', v)
    return t

x, y, z, t, u, v = 5, 10, 15, 6, 11, 16

print('Before function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('t is', t)
print('u is', u)
print('v is', v)

t = f(x, y, z, t, u, v)

print('After function f:')
print('x is', x)
print('y is', y)
print('z is', z)
print('t is', t)
print('u is', u)
print('v is', v)
