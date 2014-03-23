import itertools
import time
import math
from interchangeable import interchangeable

def naive_prime_factors(n):
    l = []
    i = 2
    while n > 1:
        while n%i == 0:
            n = n/i
            if l == [] or l[-1] is not i:
                l.append(i)
        i += 1
    return l

def primes():
    p = []
    n = 2
    while True:
        if all(n%prime != 0 for prime in p):
            yield n
            p.append(n)
        n += 1

ps = []
for p in primes():
    ps.append(p)
    if p > 3500:
        break

def pre_calculate_prime_factors(n):
    if n in ps:
        return [n]
    l = []
    for p in ps:
        if n%p == 0:
            l.append(p)
    return l

if __name__ == "__main__":
    prime_factors = interchangeable(naive_prime_factors, pre_calculate_prime_factors)
    start = time.time()
    prime_factors.learning = True
    for i in range(3500):
        print i
        prime_factors(i)
    print "learning took ", time.time() - start, " seconds"
    prime_factors.learning = False
    start = time.time()
    for i in range(3500):
        prime_factors(i)
    print "choosing took ", time.time() - start, " seconds"
    start = time.time()
    for i in range(3500):
        prime_factors(i)
    print "set only took ", time.time() - start, " seconds"
    start = time.time()
    for i in range(3500):
        naive_prime_factors(i)
    print "naive only took ", time.time() - start, " seconds"
