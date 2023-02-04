from Dessin import Dessin, applyPermutation, array2cyclic
from itertools import permutations
from sympy.combinatorics.named_groups import SymmetricGroup
from readableNestedList import readableNestedList
import time

n = 3
noniso_perm_pairs = []

b = [tuple(range(1,n+1))]
w = b
