# Problem 3: Program to find HCF of numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    a = int(input(" Input: Enter 1st Number: "))
    b = int(input("        Enter 2nd Number: "))
    hcf = gcd(a, b)
    print("Output: HCF: {}".format(hcf))

if __name__ == "__main__":
    main()


# def hcf(a, b):
#     if a < b:
#         small = a
#     else:
#         small = b
#     for i in range(1, small + 1):
#         print(i)
#         if (a % i == 0) and (b % i == 0):
#             hcf = i
#     return hcf


# a = int(input("Enter 1st Number: "))
# b = int(input("Enter 2nd Number: "))
# print(f"HCF: {hcf(a,b)}")