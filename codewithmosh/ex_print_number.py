phone = input('>')

numbers = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}
number_expansion = ""

for number in phone:
    number_expansion += numbers.get(number) + " "
print(number_expansion)