##Psuedocode
##
##x =  open('forecaster.html', 'r') //open forecaster html file as read only.
##read=x.read() //read variable set to read the x open file document
##
##lbracket = str(read.count('(')) //each of these variables initiaites a count for the specified character in the forecaster.html file
##rbracket = str(read.count(')'))
##lpointyb = str(read.count('<'))
##rpointyb = str(read.count('>'))
##lcurlyb = str(read.count('{'))
##rcurlyb = str(read.count('}'))
##lsquareb = str(read.count('['))
##rsquareb = str(read.count(']'))
##
###test print statements to console //prints statements to console
##print('Number of ( in file is: ', lbracket)
##print('Number of ) in file is: ', rbracket)
##print('Number of < in file is: ', lpointyb)
##print('Number of > in file is: ', rpointyb)
##print('Number of  { in file is: ', lcurlyb)
##print('Number of } in file is: ', rcurlyb)
##print('Number of  [ in file is: ', lsquareb)
##print('Number of  ] in file is: ', rsquareb)
##
##if lbracket != rbracket: //the following conditional statements print out error if there is an imbalance in brackets
##    print('Error: Imbalance Detected. Number of ( does not match ) there is an imbalance')
##
##if lpointyb != rpointyb:
##    print('Error: Imbalance Detected. Number of < does not match > there is an imbalance')
##
##if lcurlyb != rcurlyb:
##    print('Error: Imbalance Detected. Number of { does not match } there is an imbalance')
##
##if lsquareb != rsquareb:
##    print('Error: Imbalance Detected. Number of [ does not match ]') 
##    
##x.close() //close file after use
##
##print('Finished') //print finished at end

x =  open('forecaster.html', 'r')
read=x.read()

lbracket = str(read.count('('))
rbracket = str(read.count(')'))
lpointyb = str(read.count('<'))
rpointyb = str(read.count('>'))
lcurlyb = str(read.count('{'))
rcurlyb = str(read.count('}'))
lsquareb = str(read.count('['))
rsquareb = str(read.count(']'))

#test print statements to console
print('Number of ( in file is: ', lbracket)
print('Number of ) in file is: ', rbracket)
print('Number of < in file is: ', lpointyb)
print('Number of > in file is: ', rpointyb)
print('Number of  { in file is: ', lcurlyb)
print('Number of } in file is: ', rcurlyb)
print('Number of  [ in file is: ', lsquareb)
print('Number of  ] in file is: ', rsquareb)

if lbracket != rbracket:
    print('Error: Imbalance Detected. Number of ( does not match ) there is an imbalance')

if lpointyb != rpointyb:
    print('Error: Imbalance Detected. Number of < does not match > there is an imbalance')

if lcurlyb != rcurlyb:
    print('Error: Imbalance Detected. Number of { does not match } there is an imbalance')

if lsquareb != rsquareb:
    print('Error: Imbalance Detected. Number of [ does not match ]') 
    
x.close()

print('Finished')
    
