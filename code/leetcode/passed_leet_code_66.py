"""
WE PASSED
"""
def plusOne(digits):
    num = ''
    for char in digits:
        num += str(char)
    num_plus_one = int(num) + 1
    digits_pt_2 = []
    for char in str(num_plus_one):
        digits_pt_2.append(int(char))
    return digits_pt_2
test_cases = { [1,2,3]: [1,2,4] ,  [4,3,2,1]  : [4,3,2,2], [9]: [1,0]}
for test in test_cases:

    if plusOne(test) == test_cases[test]:
        print(f'passed {test}')
    else:
        print(f'failed {test}')