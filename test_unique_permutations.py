from unique_permutations import unique_permutations
p1 = list(unique_permutations((1,1,2,2)))
p2 = [tuple(perm) for perm in unique_permutations((1,1,2,2))]

print(p1)
print(p2)