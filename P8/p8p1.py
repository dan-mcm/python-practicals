while (True):
    x = int (input ('Please insert number:'))    
    if x < 0:
        print ('End Program')
        break
    if x % 2 == 0:
        print ('Number', x , 'is divisible by 2!')
    if x % 3 == 0:
        print ('Number', x , 'is divisible by 3!')
    if x % 5 == 0:
        print ('Number', x , 'is divisible by 5!')
    if x % 7 == 0:
        print ('Number', x , 'is divisible by 7!')
        
    
