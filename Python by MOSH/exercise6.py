numbers = [10,42,33,94,105,600,755,8,79,310]
container = 0
for counter in numbers:
  if counter > container:
    container = counter
    print(container)