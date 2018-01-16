while(True):
    x = int(input("Please insert Int:"))
    fact = 0
    if x < 0:
        print("negative int entered - program end");
        break;
    else:
        if x == 0:
            fact = 1
        elif x == 1:
            fact = 1
        else:
            fact = 1
            y = 1
            for y in range(1,x+1):
                fact *= y
        print('Factorial of', x, 'is', fact)
