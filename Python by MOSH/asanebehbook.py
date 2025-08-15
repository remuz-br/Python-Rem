str1 = 'Thirty' + 'Days' + 'Of' 'Python'
print(str1)
str2 = 'Coding' + 'For' + 'All'
print(str2)
company = 'Coding For All'
print(company)
print(len(company))
company = company.upper()
print(company)
company = company.lower()
print(company)
company = company.capitalize()
print(company)
company = company.title()
print(company)
company = company.swapcase()
print(company)
companySlice = company[0:6:1]
print(companySlice)
company = company.swapcase()
print(company.index('Coding'))
company = company.lower()
companyRep = company.replace('coding', 'Python')
print(companyRep)
companySplit = companyRep.split(' ')
print(companySplit)
stringList = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(stringList.split(','))
print(company[0])
print(company[10])
print(company[-1])
company = 'Coding For All'
company2 = 'Python For All'
company = company.title()
def createAcronym(acronymSource):
    acronym = ''
    for char in acronymSource:
        if char.isupper():
            acronym += char
    return acronym
print(createAcronym(company))
print(createAcronym(company2))
print(company.index('C'))
print(company.index('F'))
company = 'Coding For All People'
print(company.rfind('l'))
string2 = 'You cannot end a sentence with because because because is a conjunction'
print(string2.index('because'))

string3 = 'You cannot end a sentence with because because because is a conjuction'

string3split = string3.split(' ')
print(string3split)
splitResult = []
for word in string3split:
    if word != 'because':
        splitResult.append(word)

print(splitResult)
print(company.startswith('Coding'))
print(company.endswith('Coding'))

string4 = '    Coding For All   '
string4split = string4.split()
string4join = ' '.join(string4split)
print(string4join)
string5 = '30DaysOfPython'
string6 = 'thirty_days_of_python'
print(string5.isidentifier())
print(string6.isidentifier())
list1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list1Join = '-'.join(list1)
print(list1Join)
string6 = ('''I am enjoying this challenge.
i just wonder what is next''')
string6Split = string6.split('\n')
print(string6Split)
string7 = '''Name\tAge\tCountry\t\tCity
Remuel\t250\tPhilippines\tAngat'''
print(string7)

