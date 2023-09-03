# Problem 1: Program to Break list into Chunks of list

def chunk_list(list1, chunk_size):
    chunks = []
    for i in range(0, len(list1), chunk_size):
        chunks.append(list1[i : i + chunk_size])

    return chunks


def main():
    list1 = [10, 45, 20, 62, 47, 85, 12, 63, 24, 78, 10]
    chunk_size = 2
    chunks = chunk_list(list1, chunk_size)
    print("The original list:", list1)
    print("The chunks of the list:", chunks)


if __name__ == "__main__":
    main()

