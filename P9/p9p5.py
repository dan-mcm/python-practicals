while(True):
    maxTop = int(input("Please insert Max Number of Possible Toppings:")) #manager selected toppings
    selectedTop = int(input("Please insert your chosen Number of Possible Toppings:")) #standard number of toppings
    differenceTop = maxTop - selectedTop
    fact1 = 0
    fact2 = 0
    fact3 = 0
    y = 1
    z = 1
    w = 1
        
    if maxTop == 0:
        fact1 = 1
    elif maxTop == 1:
        fact1 = 1
    else:
        fact1 = 1
        y = 1
        for y in range(1,maxTop+1):
            fact1 *= y
    print('Factorial of', maxTop , 'is', fact1)


    if selectedTop > maxTop:
        print("Too many toppings selected - only", selectedTop ,"available!");
        break;
    else:
        if selectedTop == 0:
            fact2 = 1
        elif selectedTop == 1:
            fact2 = 1
        else:
            fact2 = 1
            w = 1
            for w in range(1,selectedTop+1):
                fact2 *= w
        print('Factorial of', selectedTop, 'is', fact2)

        
    if differenceTop == 0:
        fact3 = 1
    elif differenceTop == 1:
        fact3 = 1
    else:
        fact3 = 1
        z = 1
        for z in range(1,differenceTop+1):
            fact3 *= z
    print('Factorial of', differenceTop, 'is', fact3)

    combinations = fact1/(fact2*fact3)
    print("Number of combinations =",combinations)

        
