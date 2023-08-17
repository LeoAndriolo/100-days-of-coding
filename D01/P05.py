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


# import math

# def check_Perfect_Square(m):
#     semifinal = int(math.sqrt(m))
#     if pow(semifinal, 2) == m:
#         return True
#     return False


# def fibo(n):
#     t1 = 5*n*n+4
#     t2 = 5*n*n-4
#     if check_Perfect_Square(t1) or check_Perfect_Square(t2):
#         return True
#     else:
#         return False


# a = int(input("Enter a Number: "))
# if fibo(a):
#     print("Yup! It's a Fibinacci Number")
# else:
#     print("It's not a Fibonacci Number")