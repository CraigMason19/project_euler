def Eratosthenes(limit):
    primes = [True] * limit
    # 2 is the first prime
    primes[0] = primes[1] = False

    for (i, isprime) in enumerate(primes):
        if isprime:
            # Mark factors non-prime
            for factor in range(i*i, limit, i):
                primes[factor] = False

    return [i for i, n in enumerate(primes) if n == True]

def Composite(limit):
    """ A modified Eratosthenes sieve. It does the opposite and returns non primes """
    primes = [True] * limit
    # 2 is the first prime
    primes[0] = primes[1] = False

    for i, isprime in enumerate(primes):
        if isprime:
            # Mark factors non-prime
            for factor in range(i*i, limit, i):
                primes[factor] = False

    # 0 and 1 are not composite numbers
    primes[0] = primes[1] = True
    return [i for i, n in enumerate(primes) if n == False]


def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1

def Phi(n):
    """ Returns a list with totients (phi's) in the range [0 -> n-1] """
    tots = list(range(n))
    for i in range(2, n):
        if tots[i] == i:
            # Instead of removing multiples of the primes (prime sieves) we
            # need to multiply them by 1 - (1 / i)
            for j in range(i, n, i):
                tots[j] = int(tots[j] * (1 - (1/i)))

    return tots