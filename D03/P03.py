# Problem 3: Program for Searching elements in a list

def search_element(list1, element):
    index = 0
    found = False

    while index < len(list1) and not found:
        if list1[index] == element:
            found = True
        else:
            index += 1
    return index if found else -1


def main():
    list1 = [1, 2, 3, 4, 5]
    element = 5

    index = search_element(list1, element)

    if index != -1:
        print("The element {} is found at index {}.".format(element, index))
    else:
        print("The element {} is not found.".format(element))


if __name__ == "__main__":
    main()
