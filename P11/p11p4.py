#Psuedocode
#
#while(True): //allows infinite loop to reprompt user for input
#
#    n = user input //assigns variable to user input
#
#    fact1=0 //this is n factorial
#    fact2=0 //this is 2n factorial
#    fact3=0 //this is n+1 factorial
#    
#    x = 0
#    
#    if n < 0:
#        print("negative int entered - program end"); //break from loop if neg int entered
#        break;
#    
#    while(n > x): //while user input is greater than x - this allows us to list values for all items in the Catalan series
#        x += 0.0001 //exponential growth as loop runs - small decimal needed to account for this
#        
#        fact1 = 1 //sets initial values of factorials to 1
#        fact2 = 1
#        fact3 = 1
#        
#        b = 2 * n //sets 2*n to the variable b
#        a = n + 1 //sets n+1 to the variable a
#            
#        
#        fact1 = 1
#        fact2 = 1
#        fact3 = 1
#                          
#        for j in range(1,b+1): //calulates 2n factorial
#            fact2 *= j
#                
#        for k in range(1,a+1): //calculates n+1 factorial
#            fact3 *= k
#
#        for i in range(1,n+1): //calculates n factorial
#            fact1 *= i
#            
#        result = fact2/(fact3*fact1) //formula for calculating the Catalan
#        print("Catalan Number", n, "is =", result) //prints Catalan number
#        
#        n -= 1
        



while(True):

    n = int(input('Please Enter Int: '))

    fact1=0 #this is n factorial
    fact2=0 #this is 2n factorial
    fact3=0 #this is n+1 factorial
    
    x = 0
    
    if n < 0:
        print("negative int entered - program end");
        break;
    
    while(n > x):
        x += 0.0001 #exponential growth as loop runs - small decimal needed to account for this - help??
        
        fact1 = 1
        fact2 = 1
        fact3 = 1
        
        b = 2 * n
        a = n + 1
            
        
        fact1 = 1
        fact2 = 1
        fact3 = 1
                          
        for j in range(1,b+1): #2n factorial
            fact2 *= j
                
        for k in range(1,a+1): #n+1 factorial
            fact3 *= k

        for i in range(1,n+1): #n factorial
            fact1 *= i
            
        result = fact2/(fact3*fact1)
        print("Catalan Number", n, "is =", result)
        
        n -= 1
        
