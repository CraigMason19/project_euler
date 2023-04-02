#-------------------------------------------------------------------------------
# Name:        Problem 052
#
# Links:
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

def SortNumberString(n):
    return int("".join(sorted(str(n))))

def main():
    for i in range(1, 10**6):
        sns = SortNumberString(i)
        if(sns == SortNumberString(i*2)):
            if(sns == SortNumberString(i*3)):
                if(sns == SortNumberString(i*4)):
                    if(sns == SortNumberString(i*5)):
                        if(sns == SortNumberString(i*6)):
                            print(i)
                            break

if __name__ == '__main__':
    main()







