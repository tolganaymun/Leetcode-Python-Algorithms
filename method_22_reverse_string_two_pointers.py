def reverse_string_two_pointers(text):
    characters = list(text)
    left = 0
    right = len(characters) - 1
    while left < right:
        characters[left], characters[right] = characters[right], characters[left]
        left += 1
        right -= 1
    return "".join(characters)


if __name__ == "__main__":
    print(reverse_string_two_pointers("hello"))
