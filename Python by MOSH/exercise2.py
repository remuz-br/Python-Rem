housePrice = 1000000
creditScore = input('Does the buyer has good credit? ')
buyerCredit = 'yes' in creditScore
downPayment = 0
if buyerCredit == True:
  downPayment = housePrice * .1
else:
  downPayment = housePrice * .2
print(f"Down payent: ${downPayment}")