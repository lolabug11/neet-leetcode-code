def fib(n: int):
    if n == 0:return 0
    if n == 1 or n == 2: return 1
    two_numbers = [0,1]
    for i in range(n):
        next_num = two_numbers[0] + two_numbers[1]
        two_numbers[0] = two_numbers[1]
        two_numbers[1] = next_num

    return two_numbers[0]
test_cases = {0:0   , 1:1   , 2:1   , 3:2   , 4:3, 30:832040}
for test in test_cases:
    result = fib(test)
    if result == test_cases[test]:
        print(f'passed {test}')
    else:
        print(f'failed {test}')
        