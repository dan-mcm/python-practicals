##Psuedocode
##
##x = str(input('Please insert string 1:  '))  // user input 1
##y = str(input('Please insert string 2:  ')) // user input 2
##
##def  topHeavy(a,b):
##    '''function prints out true or false if one string features at end of other'''
##    a = a.lower() //converts strings to lowercase
##    b = b.lower()
##    
##    print( a[-(len(b)):] == b or a == b[-(len(a)):]) //prints out true or false depending on conditions being met
##    return
##
##
##topHeavy(x,y)
##





x = str(input('Please insert string 1:  '))
y = str(input('Please insert string 2:  '))

def  topHeavy(a,b):
    '''function prints out true or false if one string features at end of other'''
    
    a = a.lower()
    b = b.lower()
    
    print( a[-(len(b)):] == b or a == b[-(len(a)):])
    return


topHeavy(x,y)
