#-------------------------------------------------------------------------------
# Name:        Problem 017.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

NumberWords = { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
                7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',
                12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
                20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety',
                100: 'Hundred', 1000: 'Thousand' }


def WordFromNumber(n):
    if n == 0:
        return 'Zero'

    words = []
    nStr = str(n)
    length = len(nStr)

    # Simple dict lookup for 1-9
    if length == 1:
        words.append(NumberWords[n])

    # Check for 10, 11, 12 and teens
    if length >= 2:
        tmp = int(nStr[-2:])
        if 10 <= tmp <= 19:
            words.append(NumberWords[tmp])
        else:
            # units
            units = int(nStr[-1])
            if units != 0:
                words.append(NumberWords[units])

            # tens
            if length >= 2:
                tenStr = nStr[-2:]
                tens = int(tenStr[0]+'0')

                if tenStr[0] != '0':
                    words.append(NumberWords[tens])

        # hundreds
        if length >= 3:
            hundredStr = nStr[-3:]
            hundreds = int(hundredStr[0]+'00')

            if hundreds != n:
                words.append('and')
            words.append(NumberWords[100])
            words.append(NumberWords[int(hundredStr[0])])

    words.reverse()
    words = ' '.join(words)
    return words

def NumberOfLetters(s):
    return len(s.replace(' ', ''))

def main():
    answer = 0
    for i in range(1, 1000):
        answer += NumberOfLetters(WordFromNumber(i))
    answer += NumberOfLetters("One thousand")
    print(answer)

if __name__ == '__main__':
    main()