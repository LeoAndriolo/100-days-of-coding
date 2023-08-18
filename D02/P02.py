# Problem 2: Program for Array Rotation

def rotate_array(arr, n, d):
    for i in range(d):
        temp = arr[0]
        for j in range(n - 1):
            arr[j] = arr[j + 1]
        arr[n - 1] = temp

def main():
    array = []
    n = int(input("Number of elements in the array: "))
    for i in range(n):
        element = int(input("Enter element {}: ".format(i + 1)))
        array.append(element)
    
    n = len(array)
    d = int(input("Enter the rotation threshold: "))
    rotate_array(array, n, d)
    print("The rotated array is:")
    for i in range(n):
        print(array[i]," ", end="")

if __name__ == "__main__":
    main()