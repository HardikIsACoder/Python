#2. Write a program to calculate the sum of series up to n term. For example, if n =5
# the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
n = int(input("Enter n: "))
def sum(n):
    sum = 0
    curr = 2
    for i in range(0,n):
        sum += curr
        curr = curr*10 + 2
    return sum
print(sum(n))
