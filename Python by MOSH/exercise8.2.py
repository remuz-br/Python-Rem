#exercise for converting a number in a string into words using a dictionary
numberwords = {
  '1' : 'one',
  '2' : 'two',
  '3' : 'three',
  '4' : 'four',
  '5' : 'five',
  '6' : 'six',
  '7' : 'seven',
  '8' : 'eight',
  '9' : 'nine',
  '0' : 'zero'
}

phone = input('>')
result = ''
for index in phone:
  result += numberwords.get(index) + ' ' #based on the index which will match the dictionary numbers, this value will return its counterpart value in dictionary

print(result)