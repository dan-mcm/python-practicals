x = str (input('Please enter your password:'))
pas = str ('pass123')

if (x == pas):
    print("You have successfully logged in!");
else:
        print("Sorry, the password is wrong")
        a = str (input('Please enter your password 3 times:'))
        b = str (input('Please enter your password (2nd time):'))
        c = str (input('Please enter your password (3rd time):'))
        
        if (a  == pas and b == pas and c == pas):
            print("You have successfully logged in!");
        else:
            print ("You have been denied access");
        
