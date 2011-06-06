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

def divisible_by_two_through_ten(num):
    tests = [divisible_by_two,
            divisible_by_three,
            divisible_by_four,
            divisible_by_five,
            divisible_by_six,
            divisible_by_seven,
            divisible_by_eight,
            divisible_by_nine,
            divisible_by_ten,]
    return all_tests_false(num, tests)

def all_tests_false(num, tests):
    for fun in tests:
        if fun(num) == True:
            return False
    return True
