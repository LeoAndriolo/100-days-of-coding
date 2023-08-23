# Problem 1: Program to check whether list is Monotonic or not

def is_monotonic(list1):
    increasing = True
    decreasing = True

    for i in range(1, len(list1)):
        if list1[i] > list1[i - 1]:
            increasing = False
        elif list1[i] < list1[i - 1]:
            decreasing = False

    if increasing or decreasing:
        return True
    else:
        return False

def main():
    list1 = [1, 2, 3, 4, 5]
    print("The list is monotonic:", is_monotonic(list1))


if __name__ == "__main__":
    main()
