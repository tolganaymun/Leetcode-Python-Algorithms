def count_substrings_length_k(text, k):
    if k <= 0 or k > len(text):
        return 0
    return len(text) - k + 1


if __name__ == "__main__":
    print(count_substrings_length_k("hello", 2))
