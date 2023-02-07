def permute(permutation, n):
    for row in permutation:
        for i in range(len(row)):
            if row[i] == n:
                return row[(i + 1) % len(row)]

class angleRegion():
    def __init__(self, lowerBound, upperBound):
        self.lowerBound = lowerBound % 360
        self.upperBound = upperBound % 360

    def __str__(self):
        return f"({self.lowerBound}, {self.upperBound})"

    def __repr__(self):
        return f"({self.lowerBound}, {self.upperBound})"

    def withinRange(self, val):
        val = val % 360
        return (self.lowerBound < self.upperBound and self.lowerBound < val < self.upperBound) \
            or (self.lowerBound > self.upperBound and self.lowerBound < val < self.upperBound)

    def shrinkLowerBound(self, newLowerBound):
        #if self.withinRange(newLowerBound):
        #   self.lowerBound = newLowerBound % 360
        self.lowerBound = newLowerBound % 360

    def shrinkUpperBound(self, newUpperBound):
        #if self.withinRange(newUpperBound):
        #    self.upperBound = newUpperBound % 360
        self.upperBound = newUpperBound % 360

    def getClosestWithinRange(self, val):
        val = val % 360

        return val if self.withinRange(val) else self.calcDiffs(val)

    def getClosestOutsideRange(self, val):
        val = val % 360
        return self.calcDiffs(val) if self.withinRange(val) else val

    # TODO Rename this here and in `getClosestWithinRange` and `getClosestOutsideRange`
    def calcDiffs(self, val):
        lowerDiff = min(abs(360 - self.lowerBound - val), abs(val - self.lowerBound))
        upperDiff = min(abs(360 - self.upperBound - val), abs(val - self.upperBound))
        return self.lowerBound if lowerDiff < upperDiff else self.upperBound


class TwoWayDict:
    def __init__(self, right=None, left=None):

        if right is None:
            right = []
        if left is None:
            left = []
        if type(right) is dict and type(left) is dict:
            self.dictTo = right
            self.dictFrom = left
            return

        self.dictTo = dict(zip(right, left))
        self.dictFrom = {j:i for  i, j in zip(right, left)}

    def insert(self, i, j):
        self.dictTo[i] = j
        self.dictFrom[j] = i

    def keys(self):
        return self.dictTo.keys()

    def values(self):
        return self.dictFrom.keys()

    def right(self, key):
        return self.dictTo[key]

    def left(self, key):
        return self.dictFrom[key]

    def __contains__(self, key):
        return key in self.dictTo

    def __len__(self):
        return len(self.dictTo)

    def __str__(self):
        return self.dictTo.__str__()

    def __repr__(self):
        return self.dictTo.__repr__()

    def __iter__(self):
        return self.dictTo__iter__()
