"""
WE PASSED
"""
from math import *
def intToRoman(num: int) -> str:
    dec_to_roman_values = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M',
    }
    dec_to_roman_combos = {
        4: "IV",
        9: 'IX',
        40: 'XL',
        90: 'XC',
        400: 'CD',
        900: 'CM'
    }
    total = num
    num_of_IV = 0
    num_of_IX = 0
    num_of_XL = 0
    num_of_XC = 0
    num_of_CD = 0
    num_of_CM = 0
    num_of_I = 0
    num_of_V = 0
    num_of_X = 0
    num_of_L = 0
    num_of_C = 0
    num_of_D = 0
    num_of_M = 0
    num_of_M = floor(total / 1000)
    total -= num_of_M * 1000
    if floor(total/100) == 9:
        num_of_CM = 1
        total -= 900
    if floor(total/100) == 4:
        num_of_CD = 1
        total -= 400
    if floor(total/100) >= 5:
        num_of_D = 1
        total -= 500
    num_of_C = floor(total/100)
    total -= num_of_C * 100
    if floor(total/10) == 9:
        num_of_XC = 1
        total -= 90
    if floor(total/10) == 4:
        num_of_XL = 1
        total -= 40
    if floor(total/10) >= 5:
        num_of_L = 1
        total -= 50
    num_of_X = floor(total/10)
    total -= num_of_X * 10
    if total == 9:
        num_of_IX = 1
        total -= 9
    if  total >= 5:
        num_of_V = 1
        total -= 5
    if total == 4:
        num_of_IV = 1
        total -= 4

    num_of_I = floor(total)
    roman_numaral = ''
    for _ in range(num_of_M):
        roman_numaral += 'M'
    for _ in range(num_of_CM):
        roman_numaral += 'CM'
    for _ in range(num_of_D):
        roman_numaral += 'D'
    for _ in range(num_of_CD):
        roman_numaral += 'CD'
    for _ in range(num_of_C):
        roman_numaral += 'C'
    for _ in range(num_of_XC):
        roman_numaral += 'XC'
    for _ in range(num_of_L):
        roman_numaral += 'L'
    for _ in range(num_of_XL):
        roman_numaral += 'XL'
    for _ in range(num_of_X):
        roman_numaral += 'X'
    for _ in range(num_of_IX):
        roman_numaral += 'IX'
    for _ in range(num_of_V):
        roman_numaral += 'V'
    for _ in range(num_of_IV):
        roman_numaral += 'IV'
    for _ in range(num_of_I):
        roman_numaral += "I"
    return roman_numaral
test_cases = {10 :'X'}
for test in test_cases:
    result = intToRoman(test)
    if result == test_cases[test]:
        print(f'passed {test}')
    else:
        print(f'failed {test}')
        print(f'result = {result}, expected = {test_cases[test]}')
    

        

