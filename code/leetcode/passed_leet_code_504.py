"""
WE PASSED
"""


from math import *
def convertToBase7(num):
    if num == 0:
        return '0' 
        
    negative = False
    if num < 0:
        negative = True
        num *= -1
    ans = ''
    while num >= 7:
        remainder = num % 7
        num = floor(num / 7)
        ans += str(remainder)
    if num > 0:
        ans += str(num)

    if not negative:
        return ans[::-1]
    else:
        return '-' + ans[::-1]

print(convertToBase7(-7))