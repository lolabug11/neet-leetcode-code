"""
WE PASSED
"""
def isAnagram(self, s: str, t: str) -> bool:
    letters_of_s = {}
    letters_of_t = {}
    for char in s:
        if char not in letters_of_s:
            letters_of_s[char] = 1
        else:
            letters_of_s[char] += 1
    for char in t:
        if char not in letters_of_t:
            letters_of_t[char] = 1
        else:
            letters_of_t[char] += 1
    print(letters_of_s, ' = Letters of s, ', letters_of_t, ' = letters of t')
    for entry in letters_of_s:
        if entry not in letters_of_t:
            return False
        else:
            if letters_of_t[entry] != letters_of_s[entry]:
                return False
    for entry in letters_of_t:
        if entry not in letters_of_s:
            return False
        else:
            if letters_of_t[entry] != letters_of_s[entry]:
                return False
    return True