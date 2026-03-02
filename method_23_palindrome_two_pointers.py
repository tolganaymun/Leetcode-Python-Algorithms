def palindrome_two_pointers(text):
    left = 0
    right = len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(palindrome_two_pointers("madam"))
    print(palindrome_two_pointers("world"))
