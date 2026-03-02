def count_even_numbers(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count += 1
    return count


if __name__ == "__main__":
    print(count_even_numbers([1, 2, 3, 4, 6, 7]))
