#-------------------------------------------------------------------------------
# Name:        Problem 039
#
# Links:       http://en.wikipedia.org/wiki/Tree_of_primitive_Pythagorean_triples
#
# Notes:       PT or pt means Pythagorean Triplet
#              PPT or ppt means Primitive Pythagorean Triplet
#
#              Originally solved this problem using the m, n method of generating
#              ppt's but i found a better method in my solution for problem 075.
#              So i used the code from that to improve this solution. Most code
#              is from that problem
#
# TODO:
#-------------------------------------------------------------------------------

from numpy import mat, array

# Turn a NumPy 1x3 mat into a list e.g. [[3, 4, 5]] --> [3, 4, 5]
def ToList(pt):
    return pt.tolist()[0]

def Perimeter(pt):
    return sum(ToList(pt))

def AddPTToDict(d, pt):
    key = Perimeter(pt)
    tmp = ToList(pt)

    # If the key (perimeter) is in the dictionary; add this solution to the key.
    # Otherwise, we add it to the dictionary
    if key in d:
        if tmp not in d[key]:
            d[key].append(tmp)
    else:
        d[key] = [tmp]

# Using the matrix method each ppt will yield 3 different ppt's. However, this
# method will miss some multiples of previous ppt's but this is ok as we
# can work these out by multiplying them as long as they are below the perimeter
# limit
def PTSBelowPerimeter(n):
    d = { }
    l = [mat("3, 4, 5")]

    # NumPy matricies are column based
    U = mat(" 1,  2,  2; -2, -1, -2; 2, 2, 3")
    A = mat(" 1,  2,  2;  2,  1,  2; 2, 2, 3")
    D = mat("-1, -2, -2;  2,  1,  2; 2, 2, 3")

    while True:
        # Has our list been completely checked?
        if not l:
            break

        ppt = l.pop(0)
        if Perimeter(ppt) < n:
            AddPTToDict(d, ppt)

            # Add all multiples of this triple
            tmp = n // Perimeter(ppt)
            for i in range(1, tmp+1):
                AddPTToDict(d, ppt*i)

            # Generate 3 new ppts from this one and add them to our list so we
            # can generate 3 more from them
            for m in (U, A, D):
                l.append(ppt * m)

    return d

def main():
    # The first ppt is [3, 4, 5] with a perimeter of 12
    answer = 12
    ppts = PTSBelowPerimeter(10**3 + 1)

    for perimeter in ppts:
        if len(ppts[perimeter]) > len(ppts[answer]):
            answer = perimeter

    print(answer)
    print(ppts[answer])

if __name__ == '__main__':
    main()
