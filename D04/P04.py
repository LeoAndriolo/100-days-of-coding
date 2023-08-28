# Problem 4: Program for Removing Empty list

def remove_empty_values(list1):

    new_list = []
    for item in list1:
        if item:
            new_list.append(item)

    return new_list


def main():
    list1 = [5, 6, [], 7, 8, 9, [], 12, [], 4,[]]
    print("Input:", list1)
    new_list = remove_empty_values(list1)
    print("Output:", new_list)


if __name__ == "__main__":
    main()
