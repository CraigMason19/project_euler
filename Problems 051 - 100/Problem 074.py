#-------------------------------------------------------------------------------
# Name:        Problem 074
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

from math import factorial
	
Lookup = {'0':1, '1':1, '2':2, '3':6, '4':24, '5':120, '6':720, '7':5040, '8':40320, '9':362880}

def SumOfFactorialDigits(n):
	return sum(Lookup[c] for c in str(n))

def Chain(n):
	L = [n]
	tmp = n
	while(True):#
		tmp = SumOfFactorialDigits(tmp)
		if tmp in L:
			break
		if len(L) == 60:
			break
		else:
			L.append(tmp)
	return (len(L) == 60)


L = [i for i in range(1, 10**6) if Chain(i)]
print(len(L))


		
