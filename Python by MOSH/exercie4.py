#an exercise utilizing string methods and if statements
weightNum = float(input('What is your weight '))#you can convert your string input into a number datatype as long as the string is a number
unit = input('(L)for lbs and (K)for kg ').strip().lower()#strip method is used to remove whitespace like spaces and tabs and lower to converter the string into lowercase
if unit == 'l':
  weightNum /= 2.20462
  print(f"Your weight in kg is {weightNum:.2f}") #this is called an interpolation where you format a string and put braces where you want to insert a variable
elif unit == 'k':
  weightNum *= 2.20462
  print(f"Your weight in lbs is {weightNum:.2f}")
else:
  print("Invalid unit entered.")