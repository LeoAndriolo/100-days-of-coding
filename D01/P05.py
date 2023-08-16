# Problem 5: Program to check whether given number is Fibonacci or not

def is_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
        if c == n:
            return True
    return False

def main():
    n = int(input("Input: Enter a Number: "))
    if is_fibonacci(n):
        print("Output: It's a Fibonacci Number")
    else:
        print("Output: It's not an Fibonacci Number")

if __name__ == "__main__":
    main()
