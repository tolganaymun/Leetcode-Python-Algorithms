def find_max(numbers):
    if not numbers:
        return None
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum


if __name__ == "__main__":
    print(find_max([3, 8, 2, 10, 5]))
