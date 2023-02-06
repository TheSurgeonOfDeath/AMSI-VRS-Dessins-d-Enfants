from Dessin import Dessin, findMorphisms
from readableNestedList import readableNestedList

def symDes(n):
    perm = [tuple(range(1, n + 1))]
    return Dessin(perm, perm)


max_n = 20
chis = list(range(1,max_n + 1))
for i in range(1,max_n + 1):
    des = symDes(i)
    des.calcEulerChi()
    chis[i-1] = des.EulerChi
print(chis)


# # 6
# F = symDes(6)
# G = symDes(3)
# H = symDes(2)


# # calculate Euler characteristics
# F.calcEulerChi()
# G.calcEulerChi()
# H.calcEulerChi()


# # morphisms
# # morphisms = findMorphisms(F, G)
# # print(f"Mophisms: {readableNestedList(morphisms)}")
# # alpha = morphisms[1]


# # Euler Characteristic
# F.printEulerChi()
# G.printEulerChi()
# H.printEulerChi()