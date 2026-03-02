def reverse_list(items):
    reversed_items = []
    for index in range(len(items) - 1, -1, -1):
        reversed_items.append(items[index])
    return reversed_items


if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4]))
