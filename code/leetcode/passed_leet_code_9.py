"""
WE PASSED
"""
def isPalindrome(x):
    number = str(x)
    number_as_list = []
    reversed_number = ''
    for digit in number:
        number_as_list.append(digit)
    for i in range(len(number)):
        reversed_number+=number_as_list[(-i)-1]
    if number == reversed_number:
        return True
    else:
        return False