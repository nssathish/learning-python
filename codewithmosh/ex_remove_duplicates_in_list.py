numbers = [1,1,2,2,3,3,4,5,3]

##############################################################
numbers.sort()
duplicate = numbers[0]

for number in numbers[1:]:
    if number == duplicate:
        numbers.remove(number)
    else:
        duplicate = number

print(f'cleaned.. {numbers}')

##############################################################

uniques = []

for number in numbers:
    # if not uniques.count(number):
    if number not  in uniques:
        uniques.append(number)

print(f'uniques: {uniques}')