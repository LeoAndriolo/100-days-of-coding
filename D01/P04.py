# Problem 4: Program to find LCM of numbers

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    result = (a * b) // gcd(a, b)
    return result

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    result = lcm(a, b)
    print("The LCM of {} and {} is {}".format(a, b, result))

if __name__ == "__main__":
    main()
