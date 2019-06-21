class UnionFind:
    """
	Questa classe è utilizzata per implementare la struttura dati UnionFind.
	La struttura è realizzata mediante alberi con compressione del cammino.
    """

    def __init__(self, numElements):
        self.parent = list(range(numElements))
        self.rank = [0 for x in range(numElements)]

    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1

    def printParent(self):
        print("index: ", list(range(9)))
        print("parent: ", self.parent, sep='')

