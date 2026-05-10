"""
WE PASSED
"""
def func(a: str, b: str) -> str:
    int_a = int(a, base=2)
    int_b = int(b, base=2)
    sum = int_a + int_b
    bin_sum = bin(sum)[2:]
    return bin_sum



test_cases = {'test1' :['11' , '1' , '100'], 'test2':['1010','1011' , '10101'] }
for test in test_cases:

    if func(test_cases[test][0],test_cases[test][1]) == test_cases[test][2]:
        
        print(f'passed {test}')
    else:
        print(f'failed {test}')
        print(f'bin sum = {func(test_cases[test][0],test_cases[test][1])}, expected = {test_cases[test][2]}')