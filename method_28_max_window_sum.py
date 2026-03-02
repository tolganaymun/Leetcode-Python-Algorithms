def max_window_sum(numbers, k):
    if k <= 0 or k > len(numbers):
        return None
    window_sum = sum(numbers[:k])
    maximum = window_sum
    for index in range(k, len(numbers)):
        window_sum += numbers[index]
        window_sum -= numbers[index - k]
        if window_sum > maximum:
            maximum = window_sum
    return maximum


if __name__ == "__main__":
    print(max_window_sum([2, 1, 5, 1, 3, 2], 3))
