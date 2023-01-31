import utils
import itertools

class Dessin:
    def __init__(self, b, w):
        
        # Mapping edges to non-negative integers
        self.edges = set(list(itertools.chain(*b, *w)))
        self.edgeDict = utils.TwoWayDict()

        for edge in self.edges:
            if edge not in self.edgeDict:
                self.edgeDict.insert(edge, len(self.edgeDict))

        # Remapping permutations to non-negative integers
        self.black = [[self.edgeDict.right(e) for e in cycle] for cycle in b]
        self.white = [[self.edgeDict.right(e) for e in cycle] for cycle in w]

        self.size = len(self.edges)
    
    # Methods for printing the dessin
    def __str__(self):
        blackTrans = [[self.edgeDict.left(e) for e in cycle] for cycle in self.black]
        whiteTrans = [[self.edgeDict.left(e) for e in cycle] for cycle in self.white]
        return f"b: {blackTrans}, w: {whiteTrans}"
    
    def __repr__(self):
        blackTrans = [[self.edgeDict.left(e) for e in cycle] for cycle in self.black]
        whiteTrans = [[self.edgeDict.left(e) for e in cycle] for cycle in self.white]
        return f"b: {blackTrans}, w: {whiteTrans}"

    # Methods for permutations
    def permuteBlack(self, i, DS=False):
        if DS:
            return utils.permute(self.black, i)

        return self.edgeDict.left(utils.permute(self.black, self.edgeDict.right(i)))

    def permuteWhite(self, i, DS=False):
        if DS:
            return utils.permute(self.white, i)

        return self.edgeDict.left(utils.permute(self.white, self.edgeDict.right(i)))

    def permute(self, c, i, DS=False):
        if c in ["w", "white"]:
            return self.permuteWhite(i, DS=DS)

        elif c in ["b", "black"]:
            return self.permuteBlack(i, DS=DS)

        raise ValueError(f"{c} is not a valid colour. Must be 'black' or 'white'")

terminal = Dessin([(1,)], [(1,)])
