# Problem 2: Program for Cumulative Sum of list

def cumulative_func(list1):
    cumulative_sum = []
    for i in range(len(list1)):
        if i == 0:
            cumulative_sum.append(list1[i])
        else:
            cumulative_sum.append(cumulative_sum[i - 1] + list1[i])

    return cumulative_sum


def main():
    list1 = [10, 20, 30, 40, 50, 60]
    cumulative_sum = cumulative_func(list1)
    print("The original list:", list1)
    print("The cumulative sum of the list:", cumulative_sum)


if __name__ == "__main__":
    main()
