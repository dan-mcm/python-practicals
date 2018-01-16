x = str (input('Please enter your password:'))
pas = str ('pass123')

if (x == pas):
    print("You have access!");
else:
        print("Incorrect password, please try again.")
        x = str (input('Please enter your password:'))

        if (x == pas):
            print("You have access!");
        elif (x != pas):
            print("Incorrect attempt #2, 2 attempt remains.");
            x = str (input('Please enter your password:'))

            if (x == pas):
                print("You have access!");
                
            elif (x != pas):
                print("Incorrect attempt #3. 1 attempt remains.");
                x = str (input('Please enter your password:'))

                if (x == pas):
                    print("You have access!");
                elif(x != pas):
                    print("Incorrect attempt #4. Account locked.");
                     
