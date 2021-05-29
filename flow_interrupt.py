for number in range(1, 11, 1):
    if (number % 2) != 0:
        continue
    print(number)

for number in range(1, 11, 1):
    print(number)
    if number == 5:
        break
