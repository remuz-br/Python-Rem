#again, an exercise about if, elif and else statement
tempInput = input('What is the temperature today? ')
temp = int(tempInput)
if temp > 30:
  print('Its hot today right?')
elif temp < 30:
  print("Cold isn't it?")
else:
  print('Normal temp')