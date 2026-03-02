def find_index(items, target):
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    print(find_index([10, 20, 30, 40], 30))
