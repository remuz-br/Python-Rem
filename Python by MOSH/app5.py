secret_number = 9
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:
  guess = int(input('guess the number in the program '))
  guessCount += 1
  if guess == secret_number:
    print('you guess it')
    break
else:
  print('failed bastard')