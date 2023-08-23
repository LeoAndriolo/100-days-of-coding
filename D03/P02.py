# Problem 2: Program for Reversing a list

def reverse_list(list1):
    length = len(list1)
    for i in range(length // 2):
        temp = list1[i]
        list1[i] = list1[length - i - 1]
        list1[length - i - 1] = temp

    return list1


def main():
    list1 = [1, 2, 3, 4, 8]
    print("The original list:", list1)
    list1 = reverse_list(list1)
    print("The reversed list:", list1)


if __name__ == "__main__":
    main()
