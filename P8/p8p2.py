tableSize = int (input ('Please insert table size:'))
i = 1

while i <= tableSize:
    j = 1
    while j <= tableSize:
        print (i * j,  "" ,end = "")
        j += 1
    print()
    i += 1
