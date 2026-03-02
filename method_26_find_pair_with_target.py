def find_pair_with_target(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return numbers[left], numbers[right]
        if current_sum < target:
            left += 1
        else:
            right -= 1
    return None


if __name__ == "__main__":
    print(find_pair_with_target([1, 2, 3, 4, 6], 7))
