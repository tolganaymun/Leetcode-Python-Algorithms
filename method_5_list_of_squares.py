def list_of_squares(numbers):
    squares = []
    for number in numbers:
        squares.append(number * number)
    return squares


if __name__ == "__main__":
    print(list_of_squares([1, 2, 3, 4]))
