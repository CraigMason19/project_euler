#-------------------------------------------------------------------------------
# Name:        Problem 109.py
#
# Notes:
#
# Links:
#
# TODO:
#-------------------------------------------------------------------------------

class DartType:
    Single, Double, Treble = range(3)

class Dart:
    """ """
    def __init__(self, dartType, region):
        self.type = dartType
        self.region = region

        if self.type == DartType.Single:
            self.value = region
        elif self.type == DartType.Double:
            self.value = region * 2
        elif self.type == DartType.Treble:
            self.value = region * 3

    def __add__(self, other):
        if isinstance(other, int):
            return self.value + other
        if isinstance(other, Dart):
            return self.value + other.value

    def __radd__(self, other):
        if isinstance(other, int):
            return self.value + other
        if isinstance(other, Dart):
            return self.value + other.value

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        if isinstance(other, Dart):
            return self.type == other.type and self.region == other.region

    def __str__(self):
        if self.type == DartType.Single:
            return "S%d" % (self.region)
        if self.type == DartType.Double:
            return "D%d" % (self.region)
        if self.type == DartType.Treble:
            return "T%d" % (self.region)

    def __repr__(self):
        return self.__str__()
        #return "Dart(%s, %d)" % (self.type, self.region)


def main():
    singles = [Dart(DartType.Single, i) for i in range(1, 20+1)]
    doubles = [Dart(DartType.Double, i) for i in range(1, 20+1)]
    trebles = [Dart(DartType.Treble, i) for i in range(1, 20+1)]

    # Add the bullseye
    singles.append(Dart(DartType.Single, 25))
    doubles.append(Dart(DartType.Double, 25))

    # Add a empty list to each possible score. Can't finish on a 1 in darts
    checkouts = dict()
    for i in range(2, 170+1):
        checkouts[i] = []

    # There can only be 10 types of outcome invloving a double finish (M is a miss)
    # M M D     M S D
    # M D D     M T D
    # S S D     S D D
    # S T D     D D D
    # D T D     T T D
    #
    # Whenever there is a situation where the first 2 darts are of the same type
    # start the second loop fron the position of the value in the first list. e.g.
    # ... (7, 8) (7, 9) (7, 10) (7, 11) ... (8, 8) (8, 9) (8, 10, (8 11) ...
    # This allows us to avoid duplicates becauses for this problem (S1 S3 D2) is
    # considered the same as (S3 S1 D2)

    # M M D, max = 50 (D25)
    for d in doubles:
        checkouts[d.value].append((0, 0, d))

    # M S D, max = 75 (S25 + D25)
    for s in singles:
        for d in doubles:
            score = s.value + d.value
            checkouts[score].append((0, s, d))

    # M D D, max = 100 (D25 + D25)
    for d1 in doubles:
        for d2 in doubles:
            score = d1.value + d2.value
            checkouts[score].append((0, d1, d2))

    # M T D, max = 110 (T20 + D25)
    for t in trebles:
        for d in doubles:
            score = t.value + d.value
            checkouts[score].append((0, t, d))

    # S S D, max = 100 (S25 + S25 + D25)
    for i, s1 in enumerate(singles):
        for s2 in singles[i:]:
            for d in doubles:
                score = s1.value + s2.value + d.value
                checkouts[score].append((s1, s2, d))

    # S D D, max = 125 (S25 + D25 + D25)
    for s in singles:
        for d1 in doubles:
            for d2 in doubles:
                score = s.value + d1.value + d2.value
                checkouts[score].append((s, d1, d2))

    # S T D, max = 135 (S25 + T20 + D25)
    for s in singles:
        for t in trebles:
            for d in doubles:
                score = s.value + t.value + d.value
                checkouts[score].append((s, t, d))

    # D D D, max = 150 (D25 + D25 + D25)
    for i, d1 in enumerate(doubles):
        for d2 in doubles[i:]:
            for d3 in doubles:
                score = d1.value + d2.value + d3.value
                checkouts[score].append((d1, d2, d3))

    # D T D, max = 160 (D25 + T20 + D25)
    for d1 in doubles:
        for t in trebles:
            for d2 in doubles:
                score = d1.value + t.value + d2.value
                checkouts[score].append((d1, t, d2))

    # T T D, max = 170 (T20 + T20 + D25)
    for i, t1 in enumerate(trebles):
        for t2 in trebles[i:]:
            for d in doubles:
                score = t1.value + t2.value + d.value
                checkouts[score].append((t1, t2, d))

    answer = sum(len(checkouts[score]) for score in checkouts if score < 100)
    print(answer)
    #print(checkouts[123])

if __name__ == '__main__':
    main()