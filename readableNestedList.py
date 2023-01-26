def readableNestedList(nestedList):
    nestedListStr = "[\n"
    for subList in nestedList:
        nestedListStr += str(subList) + ", \n"
    nestedListStr = nestedListStr[:len(nestedListStr) - 3]
    nestedListStr += "\n]"
    return nestedListStr