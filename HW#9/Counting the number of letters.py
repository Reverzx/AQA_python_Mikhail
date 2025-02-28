def solution(text):
    stack = [text[0]]
    count = 1
    for i, char in enumerate(text[1:]):
        if stack[-1] == char:
            count += 1
            stack.append(str(count)) if count > 1 and i == len(text)-2 else 0
        else:
            stack.append(str(count)) if count > 1 else 0
            count = 1
            stack.append(char)
    return ''.join(stack)


assert solution("cccbba") == "c3b2a"
assert solution("abeehhhhhccced") == "abe2h5c3ed"
assert solution("aaabbceedd") == "a3b2ce2d2"
assert solution("abcde") == "abcde"
assert solution("aaabbdefffff") == "a3b2def5"
