# Problem 2: Program for N Largest elements in a list

def find_n_largest_elements(list1, n):

    import heapq

    heap = []
    for i in range(len(list1)):
        heapq.heappush(heap, (-list1[i], list1[i]))

    largest_elements = []
    for i in range(n):
        largest_elements.append(heapq.heappop(heap)[1])

    return largest_elements


def main():
    list1 = [4, 5, 7, 8, 9, 6, 10, 15]
    n = 4
    print("Input:", list1)
    largest_elements = find_n_largest_elements(list1, n)
    print("Output: {}".format(largest_elements))


if __name__ == "__main__":
    main()

