# Problem 1: Program to display Fibonacci Series.

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    n = int(input("Input: How Many Terms do you want to Display: "))
    print("Output: ".format(n), end="")
    for i in range(n):
        print(fibonacci(i)," ", end="")

if __name__ == "__main__":
    main()
