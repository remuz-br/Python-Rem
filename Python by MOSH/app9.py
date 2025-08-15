#exception exercise, a little similar to if statements
try: #this code block will run these lines
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)

except ZeroDivisionError: #if error encountered, will run these exception blocks instead based on the error encountered
    print('Age cannot be 0.')

except ValueError:
    print('Invalid value')