#-------------------------------------------------------------------------------
# Name:        Problem 059
#
# Links:       http://www.asciitable.com/
#
# Notes:
#
# TODO:
#-------------------------------------------------------------------------------

CipherText = []
Key = "god"

def KeyCycleGenerator():
    while(True):
        for i in range(3):
            yield Key[i]

def XOR(a, b):
    return a ^ b

def CharFromASCII(n):
    return str(chr(n))

def ASCIIFromChar(c):
    return ord(c)

def main():
    decodedText = []
    answer = 0

    # Read our ciphered text
    with open("./Problems 051 - 100/cipher1.txt", "r") as f:
        for line in f:
            CipherText = [int(i) for i in line.split(',')]

    kc = KeyCycleGenerator()

    # XOR our two numbers to get the original ASCII value
    for i, cipher in enumerate(CipherText):
        decodedASCIIValue = XOR(cipher, ASCIIFromChar(next(kc)))
        answer += decodedASCIIValue
        decodedText.append(CharFromASCII(decodedASCIIValue))
    print(''.join(decodedText), "\nTotal decoded ASCII value :", answer)

if __name__ == '__main__':
    main()
