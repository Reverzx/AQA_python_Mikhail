def solution(text: str) -> str:
    """
    This function finds the character "#" and if this character is found,
    it deletes the previous character from the string
    """
    if "#" not in text:
        return text
    else:
        if text.find("#") == 0:
            text = text[1:]
        else:
            a = text.find("#")
            text = text[:a-1]+text[a+1:]
        return solution(text)


assert solution("a#bc#d") == "bd"
assert solution("abc#d##c") == "ac"
assert solution("abc##d######") == ""
assert solution("#######") == ""
assert solution("") == ""
