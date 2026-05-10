def lengthOfLastWord(s: str) -> int:
    s +=' '
    list_of_words = []
    current_word = ''
    for char in s:
        if char != ' ':
            current_word += char
        else:
            if current_word != '':
                list_of_words.append(current_word)
                current_word = ''
    return len(list_of_words[-1])
test_cases = {'Hello World' : 5,    '   fly me   to   the moon  ': 4, 'luffy is still joyboy': 6}
for test in test_cases:

    if lengthOfLastWord(test) == test_cases[test]:
        print(f'passed {test}')
    else:
        print(f'failed {test}')