def sum_between_two_numbers(a, b):
    accumulator = 0
    for i in range(a, b + 1):
        accumulator += i

    return accumulator


if __name__ == '__main__':
    print(sum_between_two_numbers(1, 100))
    print(sum_between_two_numbers(1, 1000))