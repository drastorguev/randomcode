numbers = [1, 2, 3]


def sigma(numbers):
    sums = []
    total = 0
    for i in numbers:
        total += i
        sums.append(total)
    print sums

sigma(numbers)
