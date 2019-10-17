row_values = [6,2,2,6,2,2]

#Cheat!! Cheat!!
# for value in row_values:
#     print("X" * value)

#No cheating!! Inner loop

for value in row_values:
    row = ""
    for x in range(value):
        row += "X"
    print(row)