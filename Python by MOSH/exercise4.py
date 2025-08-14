start = 'start'
stop = 'stop'
qt = 'quit'
hlp = 'help'
indicator = 2
while True:
  indicator += 1
  user_input = input('>> ').lower
  if user_input == hlp:
    print('''start - to start the car
            stop - to stop the car
             quit - to exit ''')
  elif user_input == start:
    print('Car started broom broom')
  elif user_input == stop:
    print('Car has stopped')
  elif user_input == qt:
    print('leaving...')
    break
  else:
    print("I don't quite understand")
    