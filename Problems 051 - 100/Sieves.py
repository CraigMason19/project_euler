def Eratosthenes(limit):
    primeList = [True] * limit # Initialize the primality list
    primeList[0] = primeList[1] = False # 2 is the first prime

    for (i, isprime) in enumerate(primeList):
        if isprime:
            # yield i
            for factor in range(i*i, limit, i): # Mark factors non-prime
                primeList[factor] = False

    return [i for i, b in enumerate(primeList) if b == True]

def EratosthenesGenerator(limit):
    primeList = [True] * limit # Initialize the primality list
    primeList[0] = primeList[1] = False # 2 is the first prime

    for (i, isprime) in enumerate(primeList):
        if isprime:
            yield i
            for factor in range(i*i, limit, i): # Mark factors non-prime
                primeList[factor] = False
