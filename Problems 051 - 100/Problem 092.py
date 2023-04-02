#-------------------------------------------------------------------------------
# Name:        Problem 092
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

# The number chain in the problem is for a happy number. We are looking for all
# numbers that are NOT happy (get caught in an infinite cycle). For example, 19
# is a happy number
# 19 -> 1^2 + 9^2 = 82
# 82 -> 8^2 + 2^2 = 68
# 68 -> 6^2+ 8^2 = 100
# 100 -> 1^2 + 0^2 + 0^2 = 1.

DigitSquare = { "0":0, "1":1, "2":4, "3":9, "4":16,
                "5":25, "6":36, "7":49, "8":64, "9":81}

InfiniteCycle = [4, 16, 37, 58, 89, 145, 42, 20]

def IsHappy(n):
    while(True):
        n = sum(DigitSquare[s] for s in str(n))
        if n == 1:
            return True
        # Check for the beginning of the infinite cycle
        if n in InfiniteCycle:
            return False

def main():
    answer = sum(1 for i in range(1, 10**7) if not IsHappy(i))
    print(answer)

if __name__ == '__main__':
    main()


