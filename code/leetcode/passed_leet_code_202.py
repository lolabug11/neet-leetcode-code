"""
WE PASSED
"""


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    visited = []
    current = n
    while current not in visited:
        if current == 1: return True
        visited.append(current)
        digits = []
        for char in str(current):
            digits.append(int(char))
        current = 0
        for char in digits:
            current += char**2
    return False
test_cases = {19 : True,    2: False}
for test in test_cases:

    if isHappy(test) == test_cases[test]:
        print(f'passed {test}')
    else:
        print(f'failed {test}')