numbers = [1,2,3,4,5]

numbers.append(6)

print(numbers)

numbers.insert(3,1341234)
print(numbers)

print(numbers.pop())
print(numbers)

print(numbers.index(1341234))

# print(numbers.index(1000))
#
# print(1000 in numbers)

print(5 in numbers)

print(numbers.sort())
print(numbers)

print(numbers.count(5))

numbers2 = numbers.copy()
numbers.append(10)
print(f"numbers2: {numbers2}")

print(numbers2.reverse())
print(f'numbers2: {numbers2}')
numbers.clear()
print(numbers)
