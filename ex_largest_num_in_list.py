numbers = [1,3,4,5,10,1000]
largest = 0
for number in numbers:
    if number > largest:
        largest = number
print (f"largest number in {numbers} is: {largest}")

###################################################################
i = 0
largest = numbers[i]

while i < numbers.__len__():
    number = numbers[i]
    if number > largest:
        largest = number
    i += 1
print(f"largest number in {numbers} is: {number}")

###################################################################

max = numbers[0]
for number in numbers[1:]:
    if number > max:
        max = number

print(f"largest number in {numbers} is: {max}")