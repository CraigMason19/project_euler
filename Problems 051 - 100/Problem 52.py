def SortNumberString(n):
    return int("".join(sorted(str(n))))

for i in range(1, 1000000):
    if(SortNumberString(i) == SortNumberString(i*2)):
       if(SortNumberString(i) == SortNumberString(i*3)):
           if(SortNumberString(i) == SortNumberString(i*4)):
               if(SortNumberString(i) == SortNumberString(i*5)):
                   if(SortNumberString(i) == SortNumberString(i*6)):
                       print i
                       break
