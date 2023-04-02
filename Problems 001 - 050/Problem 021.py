#-------------------------------------------------------------------------------
# Name:        Problem 021.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

def GetSumOfFactors(n):
    return sum(i for i in range(1, (n//2)+1) if n % i == 0)

def IsAmicable(n):
    a = GetSumOfFactors(n)
    b = GetSumOfFactors(a)

    if b == n and a != b:
        return True

    return False

def main():
    answer = 0
    for i in range(1, 10**4):
        if IsAmicable(i):
            answer += i

    print(answer)

if __name__ == '__main__':
    main()