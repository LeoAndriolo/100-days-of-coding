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



# def lcm(a, b):
#     if a > b:
#         greater = a
#     else:
#         greater = b
#     while(True):
#         if(greater % a == 0) and (greater % b == 0):
#             result = greater
#             break
#         else:
#             greater += 1
#     return result


# a = int(input("Enter 1st Number: "))
# b = int(input("Enter 2nd Number: "))
# print(f"LCM of {a} and {b}: {lcm(a,b)}")