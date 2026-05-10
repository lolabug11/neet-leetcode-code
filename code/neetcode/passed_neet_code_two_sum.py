"""
WE PASSED
"""
def twoSum(nums: list[int], target: int) -> list[int]:

    len_nums = len(nums)
    for i in range(len_nums):  
        for j in range(len_nums):
            if i != j:
                if target - nums[j] == nums[i]:
                    return [i, j]
test_cases = {'test1':[[3,4,5,6] , 7, [0,1]], 'test2':[[4,5,6] , 10 , [0,2]] , 'test3' : [[5,5], 10, [0,1]]}
for test in test_cases:

    if twoSum(test_cases[test][0],test_cases[test][1]) == test_cases[test][2]:
        
        print(f'passed {test}')
    else:
        print(f'failed {test}')
        print(f'bin sum = {twoSum(test_cases[test][0],test_cases[test][1])}, expected = {test_cases[test][2]}')