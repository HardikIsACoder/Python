#5. A number is called perfect if the sum of proper divisors of that number is
#bequal to the number. For example 28 is perfect number, since
# 1+2+4+7+14=28. Write a program to print all the perfect numbers in a given range.
start = int(input("Enter the range: "))
end = int(input())
def sumDivisors(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum
def printPerfect(start, end):
    perfects = []
    for num in range(start, end + 1):
        if sumDivisors(num) == num:
            perfects.append(num)
    return perfects
if len(printPerfect(start, end)) > 0:
    print("Perfect numbers:", printPerfect(start, end))
else:
    print("No perfect numbers in the given range.")
