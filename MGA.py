from functions import Maze

n = int(input("Quanti labirinti vuoi generare? "))
for i in range(0, n):
    numRows = int(input("Inserisci il numero di righe "))
    numColumns = int(input("Inserisci il numero di colonne "))
    G = Maze.generateGraph(numRows, numColumns)
    print("Il numero dei vertici ", G.number_of_nodes())
    print("Il numero degli archi ", G.number_of_edges())
    print("L'insieme dei vertici ",G.nodes())
    print("L'insieme degli archi ",G.edges(data=True))
    T = Maze.kruskalAlgorithm(G)
    print("L'insieme degli archi del MST", T.edges())
    color1 = input("Inserisci il colore dello sfondo ")
    color2 = input("Inserisci il colore del labirinto ")
    Maze.drawMaze(T, color1, color2, numRows, numColumns)