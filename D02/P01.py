# Problem 1: Program to Check whether numbers is Armstrong or not

# Armstrong number: a number that is equal to the sum of the cubes of its own digits

def is_armstrong(n):
    num_digits = len(str(n))
    sum_of_cubes = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_cubes += digit ** num_digits
        temp //= 10
    return n == sum_of_cubes

def main():
    n = int(input("Enter a number: "))
    if is_armstrong(n):
        print("The number {} is an Armstrong number.".format(n))
    else:
        print("The number {} is not an Armstrong number.".format(n))

if __name__ == "__main__":
    main()
