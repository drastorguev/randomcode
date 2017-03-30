<<<<<<< HEAD
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
=======
numbers = [1, 2, 3]
>>>>>>> 717ec5f017c96b28bd2dbc389792f502e3034a7b


def sigma(numbers):
    sums = []
    total = 0
    for i in numbers:
        total += i
        sums.append(total)
    print sums

sigma(numbers)
