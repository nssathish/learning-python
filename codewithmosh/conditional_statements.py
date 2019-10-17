weather = input('How is the weather? ')

if weather.lower() == 'hot':
    print('''
        It's a hot day
        Drink plenty of water
    ''')
elif weather.lower() == 'cold':
    print('''
        It's a cold day
        Wear warm clothes
    ''')
else:
    print("It's a lovely day ")