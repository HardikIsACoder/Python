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
