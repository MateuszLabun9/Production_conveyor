import math

tab = []


def prime_generator(num):
    for n in range(2, num):
        prime = True
        for x in range(2, int(math.sqrt(n) + 1)):
            if n % x == 0:
                prime = False
                break
        if prime:
            tab.append(n)


def test_generator():  # tested with usage of pytest
    prime_test = True

    for x in range(2, int(math.sqrt(len(tab)) + 1)):
        if tab[x] % x == 0:
            return False

    assert prime_test == True


prime_generator(100)




