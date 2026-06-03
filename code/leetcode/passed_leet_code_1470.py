"""
WE PASSED
"""

def shuffle( nums: list[int], n: int) -> list[int]:
    x = []
    y = []
    ans = []
    for i in range(len(nums)):
        if i  < n:
            x.append(nums[i])
        else:
            y.append(nums[i])
    for i in range(len(x)):
        ans.append(x[i])
        ans.append(y[i])
    return ans