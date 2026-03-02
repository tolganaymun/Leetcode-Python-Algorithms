def most_frequent_number(numbers):
    if not numbers:
        return None
    frequency = {}
    most_frequent = numbers[0]
    highest_count = 0
    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
        if frequency[number] > highest_count:
            highest_count = frequency[number]
            most_frequent = number
    return most_frequent


if __name__ == "__main__":
    print(most_frequent_number([1, 1, 2, 2, 2, 3]))
