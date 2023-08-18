# Problem 4: Program to check whether number is Palindrome or not

def is_palindrome(n):
    # Reverse the number.
    rev_n = 0
    temp = n
    while temp > 0:
        rev_n = rev_n * 10 + temp % 10
        temp //= 10 # //= integer division operator
    # Check if the number is equal to its reverse.
    return rev_n == n


def main():
    # Prompt the user to enter a number.
    n = int(input("Enter a number: "))

    # Check if the number is a palindrome.
    check_palindrome = bool(is_palindrome(n))

    # Print whether the number is a palindrome.
    if check_palindrome:
        print("The number {} is a palindrome.".format(n))
    else:
        print("The number {} is not a palindrome.".format(n))


if __name__ == "__main__":
    main()
