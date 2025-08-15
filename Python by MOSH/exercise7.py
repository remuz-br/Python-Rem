#exercise for generating a set (a list without value repetition)
numbers = [1,1,3,5,33,7,6]
unique = []
for count in numbers:
  if count not in unique:
    unique.append(count)

print(unique)
#exercise for unpacking a list and interpolation
cantbemod = (1,2,3,4)
q,w,e,r = cantbemod
print(f'{q} {w} {e} {r}')
#exercise for a dictionary
dicto = {
  'sad' : "fuck",
  'happy' : 'stil fuck'
}
print(dicto ['sad'])