def window_sums(numbers, k):
    if k <= 0 or k > len(numbers):
        return []
    result = []
    window_sum = sum(numbers[:k])
    result.append(window_sum)
    for index in range(k, len(numbers)):
        window_sum += numbers[index]
        window_sum -= numbers[index - k]
        result.append(window_sum)
    return result


if __name__ == "__main__":
    print(window_sums([1, 2, 3, 4, 5], 3))
