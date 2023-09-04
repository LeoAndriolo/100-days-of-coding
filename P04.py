# Problem 4: Program for Flattening a list

def flatten_list(list1):
    flattened_list = []
    for item in list1:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)

    return flattened_list


def main():
    list1 = [1, 2, [3, 4, [5, 6], 7], [[[8, 9], 10]], [11, [12, 13]]]
    flattened_list = flatten_list(list1)
    print("The original list:", list1)
    print("The flattened list:", flattened_list)


if __name__ == "__main__":
    main()
