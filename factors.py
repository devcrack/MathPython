
def factors(num):
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors


def gcf(number1, number2):
    """Greatest common factor"""
    if number2 > number1:
        n1 = number2
        n2 = number1
    else:
        n1 = number1
        n2 = number2

    factors_n1 = factors(n1)
    factors_n2 = factors(n2)

    gcf = None

    for number in factors_n1:
        if number in factors_n2:
            gcf = number
    return gcf


    print()

if __name__ == '__main__':
    # print(factors(15))
    print(gcf(150, 138))