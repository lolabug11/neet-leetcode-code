"""
WE PASSED
"""
def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    roman_symbols = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}
    roman_combonations = {
        'IV':4,
        'IX':9,
        'XL':40,
        'XC':90,
        'CD':400,
        'CM':900
    }
    total = 0
    ignore_next = False
    for x in range(0,len(s)):
        if not ignore_next:
            if x == len(s)-1:
                total += roman_symbols[s[x]]
            else:
                combonation = s[x] + s[x+1]
                if combonation in roman_combonations:
                    total += roman_combonations[combonation]
                    ignore_next = True
                else:
                    total += roman_symbols[s[x]]
            print(total)
        else: 
            ignore_next = False
    return total