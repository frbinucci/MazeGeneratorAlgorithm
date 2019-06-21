import numpy as np
import networkx as nx
from UnionFind import UnionFind
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class Maze:

    '''def __init__(self, numRows, numColumns):
        self.numRows = numRows
        self.numColumns = numColumns'''

    @staticmethod
    def generateGraph(numRows, numColumns):
        h = 1
        G = nx.Graph()
        for i in range(0, numRows):
            for j in range(0, numColumns):
                G.add_node(h)
                h = h+1

        for i in G.nodes():
            if (i % numColumns != 0):
                G.add_weighted_edges_from([(i, i + 1, np.random.randint(1, 100))])

            if (i + numColumns < G.number_of_nodes()):
                G.add_weighted_edges_from([(i, i + numColumns, np.random.randint(1, 100))])

        return G

    @staticmethod
    def kruskalAlgorithm(G):
        A =[] #list empty
        u = UnionFind(G.number_of_nodes())
        sorted_edges = sorted(G.edges(data=True), key = lambda edge: edge[2]['weight'])
        for e in sorted_edges:
            if u.find(e[0]-1)!=u.find(e[1]-1):
                A.append(e)
                u.union(e[0]-1, e[1]-1)

        T = nx.Graph()
        for v in G.nodes():
            T.add_node(v)
        for e in A:
            T.add_edge(e[0], e[1])

        return T

    @staticmethod
    def drawMaze(T, color1, color2, numRows, numColumns):
        plt.figure()
        currentAxis = plt.gca()
        currentAxis.add_patch(Rectangle((0, 0), 1, 1, color=color1))

        for v in T.nodes():
            if (v % numColumns != 0):
                currentAxis.add_patch(Rectangle((0.05 + 0.9*2*((v % numColumns)-1)/(2 * numColumns-1), 0.05 + 0.9*2*(np.floor(v / numColumns))/ (2 * numRows - 1)), 0.9/(2 * numColumns-1), 0.9/(2 * numRows-1), color=color2))
            elif (v%numColumns==0):
                currentAxis.add_patch(Rectangle((0.05 + 0.9*2*(numColumns-1)/(2 * numColumns-1), 0.05 + 0.9*2*(np.floor(v / numColumns)-1)/ (2 * numRows - 1)), 0.9 / (2 * numColumns - 1), 0.9 / (2 * numRows - 1), color=color2))

        for e in T.edges():
            if((e[1]==e[0]+numColumns) and (e[0]%numColumns!=0)):
                currentAxis.add_patch(Rectangle((0.05 + 0.9*2*((e[0]%numColumns)-1)/(2*numColumns-1), 0.05 + 0.9*(2*(np.floor(e[0]/numColumns))+1)/ (2 * numRows - 1)), 0.9/(2*numColumns-1), 0.9/(2*numRows-1), color=color2))
            elif((e[1]==e[0]+numColumns) and (e[0]%numColumns==0)):
                currentAxis.add_patch(Rectangle((0.05 + 0.9 * 2 * (numColumns - 1) / (2 * numColumns - 1), 0.05 + 0.9*(2*(np.floor(e[0]/ numColumns)-1)+1)/ (2 * numRows - 1)), 0.9 / (2 * numColumns - 1), 0.9 / (2 * numRows - 1), color=color2))
            elif((e[1] == e[0] + 1) and (e[0] % numColumns != 0)):
                currentAxis.add_patch(Rectangle((0.05 + 0.9*(2*((e[0]%numColumns)-1)+1)/(2*numColumns-1), 0.05 + 0.9 * 2 * (np.floor(e[0]/ numColumns)) / (2 * numRows - 1)), 0.9 / (2 * numColumns - 1), 0.9 / (2 * numRows - 1), color=color2))

        plt.show()