def window_averages(numbers, k):
    if k <= 0 or k > len(numbers):
        return []
    result = []
    window_sum = sum(numbers[:k])
    result.append(window_sum / k)
    for index in range(k, len(numbers)):
        window_sum += numbers[index]
        window_sum -= numbers[index - k]
        result.append(window_sum / k)
    return result


if __name__ == "__main__":
    print(window_averages([1, 2, 3, 4], 2))
