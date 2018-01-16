euro_currency = float (input('Enter the number of Euro(s) to convert: '))
euro_to_pound = float (0.86)
conversion = euro_currency * euro_to_pound

if euro_currency <= 0:
    print("Amount must be >= 0. Please try again.")
else:
    print('€' , euro_currency , 'converted to pounds = ' , '£' , conversion)
