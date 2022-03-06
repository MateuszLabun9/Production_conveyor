import math


def prime_generator(num):
    for n in range(2, num):
        prime = True
        for x in range(2, int(math.sqrt(n) + 1)):
            if n % x == 0:
                prime = False
                break
        if prime:
            print(n)


prime_generator(100)
