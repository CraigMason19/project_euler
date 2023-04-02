#http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html
from fractions import *
from math import *

def ToReciprical(f):
  return Fraction(f.denominator, f.numerator)

def CFToFraction(cf):
  l = list(cf) # Lists are mutable

  l[-2] = l[-2] + Fraction(1, l[-1])  
  l.pop()
  for i in reversed(range(0, len(l)-1)):
    l[i] = l[i] + ToReciprical(l[i+1])
    l.pop()
  return l[0]

def ConvergentsForE():
  yield 2
 
  L = [2]
  loopCount, modifier = 2, 1
  while True:
    if loopCount%3 == 0:
      L.append(modifier *2)
      modifier += 1
      loopCount = 0
    else:
      L.append(1)
    yield CFToFraction(L)
    loopCount += 1

Target = 100
f = ConvergentsForE()
convergants = [next(f) for i in range(Target)]

c = convergants[Target-1] 
print(c)
print(sum(map(int,str(c.numerator))))

