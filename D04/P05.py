# Problem 5: Program for Removing Multiple Elements

def remove_multiple_elements(list1, elements_to_remove):

    new_list = []
    for item in list1:
        if item not in elements_to_remove:
            new_list.append(item)

    return new_list


def main():
    list1 = [1, 2, 3, 4, 5]
    elements_to_remove = [2, 4]
    print("Input:", list1)
    new_list = remove_multiple_elements(list1, elements_to_remove)
    print("Output:", new_list)


if __name__ == "__main__":
    main()
