x = input('What is the temperature today? ')
temp1 = 'hot' in x
temp2 = 'cold' in x
if temp1 == True:
  print('Its hot today')
  print( 'Drink Plenty of water')
elif temp2 == True:
  print('Its cold today')
  print('wear warmer clothing')
else: 
  
  print('enjoy')