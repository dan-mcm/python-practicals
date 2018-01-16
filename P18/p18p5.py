##Psuedocode
##
##x = str(input('Please insert string: ')) //take user input
##
##def xyzBot(a): //setup function
##    for i in range (len(a)): //conducts checks after each letter
##        if a[0:3] == 'xyz': //if theres a direct match straight away return true
##            print('Will Return True')
##            return True
##        elif a[i] != '.' and a[i+1:i+4] == 'xyz': //if theres no period before xyz return true
##            print ('Will Return True')
##            return True
##        else: //otherwise return false
##            print ('Will Return False')
##            return False
##
##xyzBot(x) //execute function






x = str(input('Please insert string: '))

def xyzBot(a):
    for i in range (len(a)):
        if a[0:3] == 'xyz':
            print('Will Return True')
            return True
        elif a[i] != '.' and a[i+1:i+4] == 'xyz':
            print ('Will Return True')
            return True
        else:
            print ('Will Return False')
            return False

xyzBot(x)
