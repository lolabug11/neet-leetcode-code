def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s1 = ''
    s2 = ''
    for char in s:
        if char.isalpha() or char.isnumeric():
            s1 += char.lower()
            s2 = char.lower() + s2
    print(s1)
    print(s2)
    return s1 == s2

       
            

        