# Problem 3: Program for Maximum and Minimum elements in a list

def max_min(list1):
    # Initialize the maximum and minimum values to the first element in the list.
    max_value = list1[0]
    min_value = list1[0]

    # Iterate through the list.
    for i in range(1, len(list1)):
        # If the current element is greater than the maximum value, update the maximum value.
        if list1[i] > max_value:
            max_value = list1[i]

        # If the current element is less than the minimum value, update the minimum value.
        if list1[i] < min_value:
            min_value = list1[i]

    # Return the maximum and minimum values.
    return max_value, min_value


def main():
    # Prompt the user to enter the list.
    list1 = [int(x) for x in input("Enter a list of numbers: ").split()]

    # Find the maximum and minimum values in the list.
    max_value, min_value = max_min(list1)

    # Print the maximum and minimum values in the list.
    print("The maximum value is", max_value)
    print("The minimum value is", min_value)


if __name__ == "__main__":
    main()
