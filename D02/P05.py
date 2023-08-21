# Problem 5: Program to check Prime Number using Sieve of Eratosthenes

def Sieve_of_Eratosthenes(n):
    # This function implements the Sieve of Eratosthenes algorithm to find all prime numbers less than or equal to n.

    # Create a list of all numbers from 2 to n.
    prime = [True for i in range(n + 1)]

    # Initialize the current prime number to 2.
    p = 2

    # Loop through all prime numbers less than or equal to n.
    while p <= n:
        # If the current prime number is marked as prime, mark all its multiples as non-prime.
        if prime[p] == True:
            for i in range(p * 2, n + 1, p):
                prime[i] = False

        # Increment the current prime number.
        p += 1

    # Mark the first two numbers as non-prime.
    prime[0] = False
    prime[1] = False

    # Print all prime numbers less than or equal to n.
    for i in range(n + 1):
        if prime[i]:
            print(i, end=" ")


a = int(input("Upto How Many Terms: "))
Sieve_of_Eratosthenes(a)
