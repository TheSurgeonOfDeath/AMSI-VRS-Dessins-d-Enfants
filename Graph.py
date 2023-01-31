import numpy as np
import utils
from itertools import chain, zip_longest

class Graph:
    def __init__(self, dessin):
        self.dessin = dessin
        self.nBlack = len(dessin.black)
        self.nWhite = len(dessin.white)
        
        # Generating indicies for each node
        self.nodeIndex = {}
        for i in dessin.black + dessin.white:
            self.nodeIndex[id(i)] = len(self.nodeIndex)

    def index(self, node):
        # If a perm ID is passed
        if type(node) is int:
            return self.nodeIndex[node]

        # If the perm is passed
        return self.nodeIndex[id(node)]


    def findNodeWithEdge(self, nodes, edge):
        for node in nodes:
            if edge in node:
                return self.index(node)

        raise "Could not find node!"

 
    # This could be cleaned up later
    # Probably should just iterate through everything at once
    def genImmediateConnectedNodes(self, nodesIn, connectedTo):
        return {self.index(node):{self.findNodeWithEdge(connectedTo, e) for e in node} for node in nodesIn}
    
    def colour(self, n):
        return n >= self.nBlack


    def plot(self):

        # Generate a list of edges to each node
        blackConnections = self.genImmediateConnectedNodes(self.dessin.black, self.dessin.white)
        whiteConnections = self.genImmediateConnectedNodes(self.dessin.white, self.dessin.black)
        
        connections = {x[0]:x[1] for x in chain(*zip_longest(blackConnections.items(), whiteConnections.items())) if x is not None}
        
        sortedConnections = sorted(connections.items(), key=lambda item: len(item[1]), reverse=True)

        # Getting all nodes of highest connected edges
        initialNodes = [node for node in sortedConnections if len(node[1]) == len(sortedConnections[0][1])]

        # Placing the initial Nodes

        # Format of Coordinates: {id: {pos: (-,-), offset: -, colour: -}
        arg = lambda r, i, angle, colour, offset=0, angleOffset=0: {
                  "pos"     : r * np.round(np.array([np.cos(i*angle - angleOffset), np.sin(i*angle - angleOffset)]), 1) + offset
                , "offset"  : i*angle - angleOffset
                , "colour"  : colour
        }

        angle = 2 * np.pi / len(initialNodes)
        r0 = 0 if len(initialNodes) == 1 else 1

        nodeCoords = {node[0]:arg(r0, i, angle, self.colour(node[0])) for i, node in enumerate(initialNodes)}
    
        # Recursively placing other nodes
        while len(nodeCoords) < self.nBlack + self.nWhite:
            for node in list(nodeCoords.keys()):

                remainingConnectionsToNode = connections[node] - set(nodeCoords.keys())
                if len(remainingConnectionsToNode) == 0:
                    continue

                angle = 2 * np.pi / len(remainingConnectionsToNode)
                offset = nodeCoords[node]["pos"]
                angleOffset = nodeCoords[node]["offset"]

                nodeCoords.update({n:arg(1, i, angle, self.colour(n), offset=offset, angleOffset=angleOffset) for i, n in enumerate(remainingConnectionsToNode)})

        self.nodeCoords = nodeCoords

        # Placing the edges

        # Determining average "from" angle for each node
        # I think this can be integrated more with some of the stuff above as it's very similar
        blackConnections = {self.index(node): [(edge, self.findNodeWithEdge(self.dessin.white, edge)) for edge in node] for node in self.dessin.black}
        whiteConnections = {self.index(node): [(edge, self.findNodeWithEdge(self.dessin.black, edge)) for edge in node] for node in self.dessin.white}
        connections = {i:j for i, j in list(blackConnections.items()) + list(whiteConnections.items())}

        connectionDisplacements = {i:[(e, n, nodeCoords[i]["pos"] - nodeCoords[n]["pos"]) for e, n in j] for i, j in connections.items()}
        connectionDisplacementsNorm = {i:[(e, n, p / np.linalg.norm(p)) for e, n, p in j] for i, j in connectionDisplacements.items()}
        meanAngle = {i:np.arctan2(sum([n[1] for _, _, n in j]), sum([n[0] for _, _, n in j])) for i, j in connectionDisplacementsNorm.items()}
        connectionRankings = {i:sorted(j, key=lambda x: abs(meanAngle[i] - np.arctan2(x[2][1] + np.cos(meanAngle[i]), x[2][0] + np.cos(meanAngle[i])))) for i, j in connectionDisplacementsNorm.items()}

        # Placing edges in ranking order, decreasing freedom
        minAngle = 20 
        self.edges = {}

        for node in self.dessin.black + self.dessin.white:

            index = self.index(node)
            rankings = connectionRankings[index]

            # {edge: (Ang, AllowedRegion)
            angleSpace = {edge: [None, utils.angleRegion(0, 359.9), index] for edge in node}

            for e, n, (dx, dy) in connectionRankings[index]:
                desiredAngle = (np.arctan2(dy, dx) * 360 / (2 * np.pi)) % 360
                
                entry = angleSpace[e]
                entry.append(n)
                
                angle = round(entry[1].getClosestWithinRange(desiredAngle), 1)
                entry[0] = angle, 1
                
                for i in range(1, len(node)):
                    entry = angleSpace[node[(node.index(e) + i) % len(node)]]
                    #if entry[0] is not None:
                    #    break

                    # Test and propogate this if it works
                    #if entry[1].upperBound <= angle + minAngle * i:
                    #    entry[1].upperBound = angle + minAngle * i

                    entry[1].shrinkUpperBound(angle - i * minAngle)

                for i in range(1, len(node)):
                    entry = angleSpace[node[(node.index(e) - i) % len(node)]]
                    #if entry[0] is not None:
                    #    break
                    
                    #test = utils.angleRegion(entry[1].upperBound, angle - minAngle * i)
                    #if test.withinRange(entry[1].lowerBound):
                    #    entry[1].lowerBound = angle - minAngle * i

                    # Test and propogate this if it works
                    #if entry[1].lowerBound <= angle- minAngle * i:
                    #    entry[1].lowerBound = angle - minAngle * i

                    entry[1].shrinkLowerBound(angle + i * minAngle)
                
            if index < self.nBlack:
                self.edges.update({edge:{"to": data[2], "from": data[3], "angleIn": data[0]} for edge, data in angleSpace.items()})

            else:
                for edge, data in angleSpace.items():
                    self.edges[edge]["angleOut"] = data[0]

        return

    def latex(self):

        latex = ""
        latex += "\\begin{tikzpicture}\n"
        latex += "\\begin{pgfonlayer}{nodelayer}\n"

        for i, data in self.nodeCoords.items():
            latex += f"\\node [style={'White' if data['colour'] else 'Black'}] ({i}) at {tuple(data['pos'])} {{}};\n"

        latex += "\\end{pgfonlayer}\n"

        latex += "\\begin{pgfonlayer}{edgelayer}\n"

        for data in self.edges.values():
            latex += f"\\draw [in={data['angleIn']}, out={data['angleOut']}, looseness=0.75] ({data['to']}) to ({data['from']}));\n"

        latex += "\\end{pgfonlayer}\n"
        latex += "\\end{tikzpicture}\n"

        return latex
