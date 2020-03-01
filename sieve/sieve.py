import math


def primes(limit):
    primes_tab = []
    for i in range(2, limit + 1):
        primes_tab.append(i)
    i = 2
    while i <= int(math.sqrt(limit)):
        if i in primes_tab:
            for j in range(i * 2, limit + 1, i):
                if j in primes_tab:
                    primes_tab.remove(j)
        i = i + 1

    return primes_tab