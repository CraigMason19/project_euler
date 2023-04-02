import math

L = []
for n in range(1, 100+1):
    for r in range(1, n):
        tmp = math.factorial(n) / (math.factorial(r) * (math.factorial(n-r)))
        if tmp > 1000000:
            L.append(tmp)

print len(L)            