name = input('Enter your name-  ')
nameLength = len(name)
if nameLength < 3:
  print('name must be atleast 3 characters')
elif nameLength > 50:
  print("name can be maximum of 50 characters only")
else:
  print("Looks good")