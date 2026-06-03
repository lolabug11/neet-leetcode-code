"""
WE PASSED
"""
def isSameAfterReversals( num: int) -> bool:
    reversed1 = ''
    for digit in str(num):
        reversed1 = digit + reversed1
    
    reversed1 = int(reversed1)
    reversed1 = str(reversed1)
    print(reversed1, 'reversed1')
    reversed2 = ''
    for digit in reversed1:
        reversed2 = digit + reversed2
        print(reversed2)
    print(reversed2)
    return int(reversed2) == num