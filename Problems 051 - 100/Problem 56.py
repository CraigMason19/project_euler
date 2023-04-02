import math

def SumNumberString(ns):
    return sum(int(s) for s in ns)

Answer = 0
for a in range(1, 100+1):
    for b in range(1, 100+1):
        Answer = max(SumNumberString(str(pow(a, b))), Answer) 

print Answer
