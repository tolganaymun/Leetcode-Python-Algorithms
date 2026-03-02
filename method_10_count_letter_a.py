def count_letter_a(text):
    count = 0
    for char in text.lower():
        if char == "a":
            count += 1
    return count


if __name__ == "__main__":
    print(count_letter_a("banana"))
