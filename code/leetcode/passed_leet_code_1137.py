"""
WE PASSED
"""
def tribonacci(n: int) -> int:
    past_three_nums = [0,1, 1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    for _ in range(n-2):
        new_num = past_three_nums[0] + past_three_nums[1] + past_three_nums[2]
        past_three_nums[0] = past_three_nums[1]
        past_three_nums[1] = past_three_nums[2]
        past_three_nums[2] = new_num
    return past_three_nums[2]
test_cases = {0:0   , 1:1   , 2:1   , 3:2   , 4:4   ,5:7   ,6:13   , 35: ++615693474}
for test in test_cases:

    if tribonacci(test) == test_cases[test]:
        print(f'passed {test}')
    else:
        print(f'failed {test}')
        