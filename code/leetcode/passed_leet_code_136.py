"""
WE PASSED
"""


def singleNumber(nums):
    seen_numbers = {}
    for num in range(len(nums)):
        if nums[num] in seen_numbers:
            seen_numbers[nums[num]] += 1
        else:
            seen_numbers[nums[num]] = 1
    for num in seen_numbers:
        if seen_numbers[num] == 1:
            return num

