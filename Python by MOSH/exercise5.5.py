#this exercise seems to add the value inside the writer more than necessary
writer = [5,2,5,2,2]
value = 0
for interator in writer:
  for index in writer:
    value += index
    print(value)