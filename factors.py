
def factors(num):
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors


if __name__ == '__main__':
    print(factors(15))