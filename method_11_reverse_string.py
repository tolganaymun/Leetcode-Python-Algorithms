def reverse_string(text):
    result = ""
    for index in range(len(text) - 1, -1, -1):
        result += text[index]
    return result


if __name__ == "__main__":
    print(reverse_string("cat"))
