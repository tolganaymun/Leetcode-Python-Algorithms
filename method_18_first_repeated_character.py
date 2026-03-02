def first_repeated_character(text):
    seen = set()
    for char in text:
        if char in seen:
            return char
        seen.add(char)
    return None


if __name__ == "__main__":
    print(first_repeated_character("abca"))
