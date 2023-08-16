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
