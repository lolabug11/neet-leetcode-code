"""
WE PASSED
"""
def climbStairs(n: int) -> int:
    past_two_nums = [0,1]
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 1
    while i <= n:
        new_num = past_two_nums[0] + past_two_nums[1]
        past_two_nums[0] = past_two_nums[1]
        past_two_nums[1] = new_num
        i += 1
    return past_two_nums[1]
test_cases = {0:0   , 1:1   , 2:2   , 3:3   , 4:5   ,5:8   ,6:13   , 43:701408733}
for test in test_cases:

    if climbStairs(test) == test_cases[test]:
        print(f'passed {test}')
    else:
        print(f'failed {test}')