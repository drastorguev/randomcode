numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sigma(numbers):
    sums = []
    total = 0
    for i in numbers:
        total += i
        sums.append(total)
    print sums

sigma(numbers)
