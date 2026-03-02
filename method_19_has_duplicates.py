def has_duplicates(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False


if __name__ == "__main__":
    print(has_duplicates([1, 2, 3, 2]))
