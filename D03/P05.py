# Problem 5: Program to Swap first element with last element in a list

def swap_first_last_element(list1):
    temp = list1[0]
    list1[0] = list1[-1]
    list1[-1] = temp

    return list1


def main():
    list1 = [10, 5, 2, 6, 3, 7, 9, 4]
    print("The original list:", list1)
    list1 = swap_first_last_element(list1)
    print("The list after swapping the first and last element:", list1)


if __name__ == "__main__":
    main()
