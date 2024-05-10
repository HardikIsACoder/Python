#1. Write a program to display only those numbers from a list that satisfy the followingconditions
#The number must be divisible by five. If the number is greater than 150, then skip it
#and move to the next number. If the number is greater than 500, then stop the loop.
#Given: numbers = [12, 75, 150, 180, 145, 525, 50]
numbers = [12, 75, 150, 180, 145, 525, 50]
def display(list):
    for num in list:
        if num > 500:
            break
        if num > 150:
            continue
        if num%5 == 0:
            print(num)
display(numbers)
