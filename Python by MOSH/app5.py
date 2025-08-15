#exercise in the form of guessing game, loop will run until the guess will equal the secret_number
secret_number = 9
guessCount = 0
guessLimit = 3
while guessCount < guessLimit:#number of guess tries
  guess = int(input('guess the number in the program '))#the user has to type the number input
  guessCount += 1
  if guess == secret_number:
    print('you guess it')
    break #would break the loop if statement is true
else:#would stop the loop based on the limit
  print('failed bastard')