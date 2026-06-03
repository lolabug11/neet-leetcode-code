"""
WE PASSED
"""

def findMaxConsecutiveOnes(nums: list[int]) -> int:
    nums.append(0)
    longest = 0
    current = 0
    for x in nums:
        if x == 1:
            current += 1
        else:
            if longest < current:
                longest = current
            current = 0
    return longest
    