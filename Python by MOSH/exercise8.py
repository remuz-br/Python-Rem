#a really simple dictionary exercise
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
number = input('enter a number')
numberlist = list(number)

for index in numberlist:
  if index in number:
    print(numberwords[index])