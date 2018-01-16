amount = float (input('Enter the initial amount you wish to use: '))
ratio60 = (amount/100) * 60
ratio40 = (amount/100) * 40
taxratelarge = (ratio60/100) * 23
taxratesmall = (ratio40/100) * 41
totaltax = taxratelarge + taxratesmall
totalamount = totaltax + amount

if amount <= 0.0:
    print("Amount of income must be >=0. Please try again.")
else:
    print('The initial amount is = ', amount)
    print('The Ratio 60:40 works out at: ' , ratio60 , ':' , ratio40)
    print('Tax applied at the upper rate is: ', taxratelarge)
    print('Tax applied at the lower rate is: ', taxratesmall)
    print('Total taxes are: ', totaltax)
    print('Initial Amount & Taxes = ', totalamount)
    
