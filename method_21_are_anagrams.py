def are_anagrams(first, second):
    return sorted(first) == sorted(second)


if __name__ == "__main__":
    print(are_anagrams("listen", "silent"))
