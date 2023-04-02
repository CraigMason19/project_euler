def IsIncreasing(n):
    s = str(n)
    for i in range(0, len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True
        
def IsDecreasing(n):
    s = str(n)
    for i in range(0, len(s)-1):
        if s[i] < s[i+1]:
            return False
    return True

def IsBouncy(n):
    if IsIncreasing(n) or IsDecreasing(n):
        return False
    else:
        return True

#print(IsIncreasing(134668))
#print(IsDecreasing(66420))
#print(IsBouncy(155349))

import time
StartTime = time.time()

Num = 100
Count = 0
Percent = 0
while(Percent < 99.0):
    Num += 1
    if IsBouncy(Num):
        Count += 1
    Percent = Count / Num * 100

print("Number before limit", Num)
print("Total bouncy numbers", Count)
print(time.time()-StartTime)