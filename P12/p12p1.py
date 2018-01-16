#Psuedocode
#x = user input //sets user input to variable x
#fact1 = 0 //factorial variable
#
#def function(a): //defines function
#    if x < 0:
#        print("Negative int entered - program end"); //if neg int function returns None
#        return;
#    else:
#        if x == 0:
#            fact1 = 1 //if input 0 fact is 1
#        elif x ==1:
#            fact1 = 1 //if input 1 fact is 1
#        else:
#            fact1 = 1 //else fact is 1 and...
#
#            i=1
#            for i in range(1,x+1): //for loop calculates factorial
#                fact1 *= i
#            print('Factorial of ', x , 'is', fact1) //print factorials
#
#function(x) //runs function with x (user input)

x = int(input('Insert argument: '))
fact1 = 0

def function(a):
    if x < 0:
        print("Negative int entered - program end");
        return;
    else:
        if x == 0:
            fact1 = 1
        elif x ==1:
            fact1 = 1
        else:
            fact1 = 1

            i=1
            for i in range(1,x+1):
                fact1 *= i
            print('Factorial of ', x , 'is', fact1)

function(x)
