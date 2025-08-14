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


