#4. Write a function prodDigits() that inputs a number and returns the product of digits of that number.
n = int(input("Enter: "))
def prodDigits(n):
    prod = 1
    for digit in str(n):
        prod *= int(digit)
    return prod
print("Product: ", prodDigits(n))
