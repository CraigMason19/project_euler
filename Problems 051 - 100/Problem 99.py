#http://math.stackexchange.com/questions/8308/working-with-large-exponents
#
# ab > cd
# log(ab) > log(cd)
# blog(a) > dlog(c)

from math import log

class LargePower:
    def __init__(self, b=None, e=None):
        self.mBase = b
        self.mExponent = e
    def __str__(self):
        return "["+str(self.mBase)+"^"+str(self.mExponent)+"]"
    def CreateFromList(l):
        return LargePower(l[0], l[1])

def IsBigger(a, b):
    return (a.mExponent*log(a.mBase) > b.mExponent*log(b.mBase)) 

BiggestNum = LargePower(1,1)
LineNumber = 0
i = 0

f = open("base_exp.txt")
for line in f:
    i += 1
    tmpNum = LargePower.CreateFromList([int(s) for s in line.split(",")])
    if IsBigger(tmpNum, BiggestNum):
        BiggestNum = tmpNum
        LineNumber = i

print(BiggestNum, "Line", LineNumber)

        
           
    
    
