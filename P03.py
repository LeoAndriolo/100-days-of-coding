# Problem 3: Program to print Duplicates in list

def find_duplicates(list1):
    seen = set()
    duplicates = []
    for item in list1:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)

    return duplicates


def main():
    list1 = [4, 5, 1, 2, 6, 5, 2]
    duplicates = find_duplicates(list1)
    print("The original list:", list1)
    print("The duplicates in the list are:", duplicates)


if __name__ == "__main__":
    main()
