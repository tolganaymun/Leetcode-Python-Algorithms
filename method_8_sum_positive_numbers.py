def sum_positive_numbers(numbers):
    total = 0
    for number in numbers:
        if number > 0:
            total += number
    return total


if __name__ == "__main__":
    print(sum_positive_numbers([-2, 4, -1, 6, 3]))
