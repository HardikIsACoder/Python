n = int(input("Enter the number: "))
def factors(n):
    fact = []
    while n%2 == 0:
        fact.append(2)
        n /= 2
    i = 3
    while i <= n:
        while n%i == 0:
            fact.append(i)
            n /= i
        i += 2
    if n>2:
        fact.append(n)
    return fact
print("Prime factors:", factors(n))
