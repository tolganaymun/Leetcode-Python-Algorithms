def move_zeros_to_end(numbers):
    non_zeros = []
    zero_count = 0
    for number in numbers:
        if number == 0:
            zero_count += 1
        else:
            non_zeros.append(number)
    for _ in range(zero_count):
        non_zeros.append(0)
    return non_zeros


if __name__ == "__main__":
    print(move_zeros_to_end([0, 1, 0, 3, 12]))
