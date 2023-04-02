from operator import itemgetter
import collections # For collections.Counter, requires minimum
                   # Python 3.1

D = {}
for i in range(300, 10000):
    #if 
    D[i] = ''.join(sorted(str(i*i*i)))

#print(sorted(D.items(), key=itemgetter(1)))
common = collections.Counter(D.values()).most_common(2)
L = [x for x in D if D[x] == common[0][0]]
#print(L, pow(L[0], 3))
L = [x for x in D if D[x] == common[1][0]]
#print(L, pow(L[0], 3))

cubes = [sorted(str(x**3)) for x in range(10000)]
counts = [cubes.count(x) for x in cubes]
print(counts.index(5)**3)

