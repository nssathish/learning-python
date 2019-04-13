def find_max(numbers):
    max_num = numbers[0]
    
    for number in numbers[1:]:
        if number > max_num:
            max_num = number
    
    return max_num
