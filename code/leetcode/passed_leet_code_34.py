"""
WE PASSED
"""
def searchRange(nums: list[int], target: int) -> list[int]:
    start_and_end_keys = []
    for key in range(len(nums)):
        if nums[key] == target:
            start_and_end_keys.append(key)
    if start_and_end_keys != []:
        return [start_and_end_keys[0], start_and_end_keys[-1]]
    else:
        return [-1,-1]
test_cases = {'test1':[[5,7,7,8,8,10] , 8 , [3,4]],'test2':[[5,7,7,8,8,10] , 6 , [-1,-1]], 'test3':[[], 0 , [-1,-1]],  }
for test in test_cases:

    if searchRange(test_cases[test][0],test_cases[test][1]) == test_cases[test][2]:
        
        print(f'passed {test}')
    else:
        print(f'failed {test}')
        print(f'bin sum = {searchRange(test_cases[test][0],test_cases[test][1])}, expected = {test_cases[test][2]}')
            
        