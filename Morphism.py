from LDessin import Dessin
from itertools import permutations

class Morphism:
    def __init__(self, F: Dessin, G: Dessin, alpha: dict, DS=False):

        # Checking F and G datatypes
        assert type(F) is Dessin, TypeError("F must be a dessin")
        assert type(G) is Dessin, TypeError("G must be a dessin")
        
        self.F = F
        self.G = G

        # Ensuring alpha has correct domain and codomain
        assert type(alpha) is dict, TypeError("Alpha must be a dictionary")

        # If alpha is already in DS, no need to process alpha
        if DS:
            assert set(alpha.keys()) == set(range(F.size)), "Alpha has wrong domain"
            assert set(alpha.values()) == set(range(G.size)), "Alpha has wrong codomain"
            self.alpha = alpha

            return
        
        # Process alpha into DS
        assert set(alpha.keys()) == F.edges, "Alpha has wrong domain"
        assert set(alpha.values()) == G.edges, "Alpha has wrong codomain"

        FED = self.F.edgeDict.right
        GED = self.G.edgeDict.right

        self.alpha = {FED(i):GED(j) for i,j in alpha.items()}

    def __str__(self):
        FED = self.F.edgeDict.left
        GED = self.G.edgeDict.left

        alpha = {FED(i):GED(j) for i,j in self.alpha.items()}
        return str(alpha)

    def __repr__(self):
        FED = self.F.edgeDict.left
        GED = self.G.edgeDict.left

        alpha = {FED(i):GED(j) for i,j in self.alpha.items()}
        return str(alpha)

    def isValid(self):
        for e in range(self.F.size):

            if self.alpha[self.F.permuteWhite(e, DS=True)] != self.G.permuteWhite(self.alpha[e], DS=True):
                return False

            elif self.alpha[self.F.permuteBlack(e, DS=True)] != self.G.permuteBlack(self.alpha[e], DS=True):
                return False

        return True

    # Should fix this one up later
    def isValidVerbose(self):
        status = True
        for e in self.F.edges:

            if self.alpha[self.F.permuteWhite(e)] != self.G.permuteWhite(self.alpha[e]):
                print(f"Fails on White Edge {e}!")
                status = False

            elif self.alpha[self.F.permuteBlack(e)] != self.G.permuteBlack(self.alpha[e]):
                print(f"Fails on Black Edge {e}!")
                status = False

            else:
                print(f"Works on Edge {e}")

        return status

    def findMorphisms(F, G):
        nEdgesF = F.size
        nEdgesG = G.size
        
        # Checking fibre's condition
        if nEdgesF % nEdgesG != 0:
            return []

        # Generating all possible morphisms
        t = int(nEdgesF / nEdgesG)

        maps = permutations(list(range(G.size)) * t)
        # Removing duplicate maps
        maps = {d:None for d in maps}.keys()

        # Creating all morphisms
        morphisms = [Morphism(F, G, {i:j for i,j in enumerate(m)}, DS=True) for m in maps]

        return [m for m in morphisms if m.isValid()]
