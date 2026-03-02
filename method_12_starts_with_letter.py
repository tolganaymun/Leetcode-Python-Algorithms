def starts_with_letter(text, letter):
    if text == "" or letter == "":
        return False
    return text[0] == letter


if __name__ == "__main__":
    print(starts_with_letter("Apple", "A"))
