from itertools import product
from readableNestedList import readableNestedList
from itertools import chain, combinations
from sympy.combinatorics import Permutation

from Dessin2 import Dessin
from readableNestedList import readableNestedList

from sympy.combinatorics import Permutation
from sympy import init_printing
init_printing(perm_cyclic=True, pretty_print=False)

# fat square
fb = Permutation(1,2,0,3)(5,6,4,7)
fw = Permutation(0,6,1,7)(3,4,2,5)
F = Dessin(fb, fw)
F.b

fwb = F.b*F.w

F.b.array_form
F.b.cyclic_form

F.isConnected()

F.printEulerChi()
hasattr(F, 'EulerChi')