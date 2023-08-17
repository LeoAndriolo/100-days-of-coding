# Problem 1: Program to display Fibonacci Series

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    n = int(input("Input: How Many Terms do you want to Display: "))
    print("Output: ", end="")
    for i in range(n):
        print(fibonacci(i)," ", end="")

if __name__ == "__main__":
    main()

# def fibo(a):
#     m, n = 0, 1
#     count = 0
#     if a <= 0:
#         print("Alert! Wrong Input")
#     elif a == 1:
#         print(f"Fibonacci Series: {m}")
#     else:
#         print(f"Fibonacci Series: ", end="")
#         while count < a:
#             count += 1
#             print(m, end=" ")
#             nth = m+n
#             m = n
#             n = nth

# a = int(input("How Many Terms do you want to Display: "))
# fibo(a)