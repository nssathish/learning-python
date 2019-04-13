weight = float(input('Weight: '))
unit = input('(L)bs or (K)gs? ')

if unit.upper() == 'L':
    converted = weight * 0.45
    print (f"You have {converted} kilos")
else:
    converted = weight / 0.45
    print (f'You have {converted} lbs')
