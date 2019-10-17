try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age

    print (f'Age: {age} and risk: {round(risk)}')
except ValueError:
    print('Invalid Age')
except ZeroDivisionError:
    print('Age cannot be 0')