def divisible_by_two(num):
    return str(num)[-1] in ['2','4','6','8']

def divisible_by_three(num):
    return sum([int(i) for i in str(num)]) % 3 == 0

def divisible_by_four(num):
    return int(str(num)[-2:]) % 4 == 0

def divisible_by_five(num):
    return str(num)[-1] in ['0','5']

def divisible_by_six(num):
    return divisible_by_two(num) and divisible_by_three(num)

def divisible_by_seven(num):
    # I don't have a good implementation yet for this one
    return num % 7 == 0

def divisible_by_eight(num):
    return int(str(num)[-3:]) % 8 == 0

def divisible_by_nine(num):
    return sum([int(i) for i in str(num)]) % 9 == 0

def divisible_by_ten(num):
    return str(num)[-1] == '0'
