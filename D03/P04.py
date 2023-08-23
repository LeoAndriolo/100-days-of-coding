# Problem 4: Program for Second Largest element in a list

def second_largest(list1):
    length = len(list1)

    # Find the largest element in the list.
    largest = list1[0]
    for i in range(1, length):
        if list1[i] > largest:
            largest = list1[i]

    # Initialize the second largest element to the first element in the list.
    second_largest = list1[0]

    # Loop through the list and find the second largest element.
    for i in range(1, length):
        if list1[i] > second_largest and list1[i] != largest:
            second_largest = list1[i]

    return second_largest


def main():
    list1 = [7, 6, 5, 3, 2, 6, 5, 10]
    print("The second largest element in the list is:", second_largest(list1))


if __name__ == "__main__":
    main()
