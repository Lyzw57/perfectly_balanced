def check_if_balanced(phrase: str):
    letters = set(phrase)
    letters = tuple(letters)

    for i in range(len(letters) -1):
        if phrase.count(letters[i]) != phrase.count(letters[i + 1]):
            return False

    return True


print(check_if_balanced("xxxyyyzzz"))
print(check_if_balanced("abccbaabccba"))
print(check_if_balanced("abcdefghijklmnopqrstuvwxyz"))
print(check_if_balanced("pqq"))
print(check_if_balanced("fdedfdeffeddefeeeefddf"))
print(check_if_balanced("www"))
print(check_if_balanced("x"))
print(check_if_balanced(""))
print(check_if_balanced("xxxyyyzzzz"))

