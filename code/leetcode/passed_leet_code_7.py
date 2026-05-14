"""
WE PASSED
"""
def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """                       
    if x > 2147483648 or x < -2147483648:

        return 0
    negative = False
    if x < 0:
        negative =  True
        x *= -1
    x = str(x)
    x = x[::-1]
    x = int(x)

    if negative:
        return x * -1
    return x