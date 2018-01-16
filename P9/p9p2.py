while(True):
    x = int(input("Please insert Int:"))
    counter = 0

    if x < 0:
        print("negative int entered - program end");
        break;

    for y in range(1,x+1):
        counter += x;
        x -= 1;
        y += 1;
    
    print("Total is:", counter)
    
