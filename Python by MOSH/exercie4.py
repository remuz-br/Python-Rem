weightNum = float(input('What is your weight '))
unit = input('(L)for lbs and (K)for kg ').strip().lower()
if unit == 'l':
  weightNum /= 2.20462
  print(f"Your weight in kg is {weightNum:.2f}")
elif unit == 'k':
  weightNum *= 2.20462
  print(f"Your weight in lbs is {weightNum:.2f}")
else:
  print("Invalid unit entered.")