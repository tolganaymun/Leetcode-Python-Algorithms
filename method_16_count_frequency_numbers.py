def count_frequency_numbers(numbers):
    frequency = {}
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    return frequency


if __name__ == "__main__":
    print(count_frequency_numbers([1, 1, 2, 3, 3, 3]))
