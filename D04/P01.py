# Problem 1: Program for Cloning/Copying the list

def clone_list(list1):
    list2 = []
    for item in list1:
        list2.append(item)

    return list2


def main():
    list1 = [1, 2, 3, 4, 6]
    print("The original list:", list1)
    list2 = clone_list(list1)
    print("The cloned list:", list2)


if __name__ == "__main__":
    main()
