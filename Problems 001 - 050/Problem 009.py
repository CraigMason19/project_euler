#-------------------------------------------------------------------------------
# Name:        Problem 009.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

def main():
    for a in range(1, 500+1):
        for b in range(1, 500+1):
            c = 1000 - a - b;
            if(a*a + b*b == c*c):
                print(a, b, c, "Product is ", a*b*c)
                return

if __name__ == '__main__':
    main()