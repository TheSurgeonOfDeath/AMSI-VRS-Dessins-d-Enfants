from permute import permute

alpha = [1, 1, 2, 2, 3, 3, 4, 4]
fw = [(1, 8, 7, 2), (3,4,5,6)]
fb = [(1,2,4,3), (7,8,6,5)]
gw = [(1,4), (2,3)]
gb = [(1,2), (3,4)]

for e in range(1, len(alpha)+1):
    #alpha fb = gb alpha
 
    if alpha[permute(fw, e)-1] != permute(gw, alpha[e-1]):
        print(f"Fails on White Edge {e}!")
        #break 

    elif alpha[permute(fb, e)-1] != permute(gb, alpha[e-1]):
        print(f"Fails on Black Edge {e}!")
        #break

    else:
        print(f"Works on Edge {e}")
