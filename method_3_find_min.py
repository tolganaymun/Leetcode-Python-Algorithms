def find_min(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum


if __name__ == "__main__":
    print(find_min([3, 8, 2, 10, 5]))
