n = int(input("Enter n: "))
def sum(n):
    sum = 0
    curr = 2
    for i in range(0,n):
        sum += curr
        curr = curr*10 + 2
    return sum
print(sum(n))
