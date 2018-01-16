##Psuedocode
##x =  open('index.html', 'r') //open file in read only mode
##read=x.read() //set variable read to read the x file
##
##y = open('test.txt','w') //opens test file to write to
##
##a = str(read.count('<')) //casts the counts to strings as python throws error if int
##b = str(read.count('>'))
##c = str(read.count('\n'))
##d = str(read.count('<!--'))
##e = str(read.count('-->'))
##f = str(read.count('e'))
##
##y.write('Number of < in file is: ' + a + '\n') //write statements to file
##y.write('Number of > in file is: ' + b + '\n')
##y.write('Number of newlines in file is: ' + c + '\n')
##y.write('Number of <!-- in file is: ' + d + '\n')
##y.write('Number of  --> in file is: ' + e + '\n')
##y.write('Number of  lowercase e in file is: ' + f + '\n')
##
###test print statements to console
##print('Number of < in file is: ', a) //bunch of test print statements
##print('Number of > in file is: ', b)
##print('Number of newlines in file is: ', c)
##print('Number of <!-- in file is: ', d)
##print('Number of  --> in file is: ', e)
##print('Number of  lowercase e in file is: ', f)
##    
##x.close() //close x file
##y.close() //close y file
##
##print('Finished')
##    

x =  open('index.html', 'r')
read=x.read()

y = open('test.txt','w')

a = str(read.count('<'))
b = str(read.count('>'))
c = str(read.count('\n'))
d = str(read.count('<!--'))
e = str(read.count('-->'))
f = str(read.count('e'))

y.write('Number of < in file is: ' + a + '\n')
y.write('Number of > in file is: ' + b + '\n')
y.write('Number of newlines in file is: ' + c + '\n')
y.write('Number of <!-- in file is: ' + d + '\n')
y.write('Number of  --> in file is: ' + e + '\n')
y.write('Number of  lowercase e in file is: ' + f + '\n')

#test print statements to console
print('Number of < in file is: ', a)
print('Number of > in file is: ', b)
print('Number of newlines in file is: ', c)
print('Number of <!-- in file is: ', d)
print('Number of  --> in file is: ', e)
print('Number of  lowercase e in file is: ', f)
    
x.close()
y.close()

print('Finished')
    
