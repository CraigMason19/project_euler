#modular exponentiation algorithm

import sys
sys.path.append('F:\Programming\Python\Project Euler')

import PEHelper

def ToBinary(n):
    return bin(n)[2:]

def BinaryToPowers2(binaryString):    
    l = []
    tmp = 1
    for char in binaryString[::-1]:
        if char == '1':
            l.append(tmp)
        tmp *= 2
    l.reverse()
    return l


B = ToBinary(7830457)
L = BinaryToPowers2(B)
print(B)
print(L)

#def ModExp(b, e, m) :


a = 28433 * pow(2,7830457,10**10) + 1
print(str(a)[-10:])


