def remove_duplicates_sorted(numbers):
    if not numbers:
        return []
    result = [numbers[0]]
    for number in numbers[1:]:
        if number != result[-1]:
            result.append(number)
    return result


if __name__ == "__main__":
    print(remove_duplicates_sorted([1, 1, 2, 2, 3]))
