"""
multiple inputs
"""
def func(input1, input2):
    pass
test_cases = {'test1':['input1' , 'input2' , 'result'], 'test2':['input1' , 'input2' , 'result'] }
for test in test_cases:

    if func(test_cases[test][0],test_cases[test][1]) == test_cases[test][2]:
        
        print(f'passed {test}')
    else:
        print(f'failed {test}')
        print(f'bin sum = {func(test_cases[test][0],test_cases[test][1])}, expected = {test_cases[test][2]}')
"""
One input
"""        
result = None
def func(inupt):
    pass
test_cases = {'test1' : result,    'test2': result, 'test3': result}
for test in test_cases:

    if func(test) == test_cases[test]:
        print(f'passed {test}')
    else:
        print(f'failed {test}')