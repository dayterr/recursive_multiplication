import argparse 


def rec_mult(number1, number2):
    l1 = len(str(number1))
    l2 = len(str(number2))
    n = max(l1, l2)
    m = n // 2
    if number1 < 10 and number2 < 10:
        return number1 * number2
    a, b = number1 // 10 ** m, number1 % 10 ** m
    c, d = number2 // 10 ** m, number2 % 10 ** m
    p = a + c
    q = b + d
    ac = rec_mult(a, c)
    ad = rec_mult(a, d)
    bc = rec_mult(b, c)
    bd = rec_mult(b, d)
    return (10 ** (m * 2)) * ac + (10 ** (n // 2) * (ad + bc)) + bd
    

def karatsuba(number1, number2):
    l1 = len(str(number1))
    l2 = len(str(number2))
    n = max(l1, l2)
    m = n // 2
    if number1 < 10 and number2 < 10:
        return number1 * number2
    a, b = number1 // 10 ** m, number1 % 10 ** m
    c, d = number2 // 10 ** m, number2 % 10 ** m
    p = a + b
    q = c + d
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    pq = karatsuba(p, q)
    adbc = pq - ac - bd
    return 10 ** (m * 2) * ac + 10 ** m * adbc + bd


def main():
    parser = argparse.ArgumentParser(description='Process two multipliers')
    parser.add_argument('first', type=int, help='first_multiplier')
    parser.add_argument('second', type=int, help='second_multiplier')
    args = parser.parse_args()
    first = args.first
    second = args.second
    rec = rec_mult(first, second)
    kar = karatsuba(first, second)
    print(f'recursive multiplication algorithm: {rec}')
    print(f'Karatsuba algorithm: {rec}')


if __name__ == '__main__':
    main()