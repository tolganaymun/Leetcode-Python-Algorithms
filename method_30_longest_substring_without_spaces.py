def longest_substring_without_spaces(text):
    current_length = 0
    max_length = 0
    for char in text:
        if char == " ":
            current_length = 0
        else:
            current_length += 1
            if current_length > max_length:
                max_length = current_length
    return max_length


if __name__ == "__main__":
    print(longest_substring_without_spaces("ab cd efg"))
