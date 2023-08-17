# Problem 2: Program to find Factorial of number

def factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    n = int(input("Input: Enter a Number: "))
    print("Output: {}! = {}".format(n, factorial(n)))

if __name__ == "__main__":
    main()

# def factorial(n):
#     return 1 if (n == 0 or n == 1) else n*factorial(n-1)

# n = int(input("Enter a Number: "))
# print(f"{n}! = {factorial(n)}")