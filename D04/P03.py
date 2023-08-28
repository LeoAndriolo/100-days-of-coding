# Problem 3: Program for Occurrences of elements

def count_occurrences(list1, element):

    count = 0
    for i in range(len(list1)):
        if list1[i] == element:
            count += 1

    return count


def main():
    list1 = [14, 25, 16, 23, 10, 5, 6, 8, 7, 9, 10, 25, 14]
    element = 14
    print("Input:", list1)
    count = count_occurrences(list1, element)
    print("Output: {} Occurs {} times".format(element, count))


if __name__ == "__main__":
    main()
