from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from datetime import datetime
from UnionFind import UnionFind
from functions import Maze
'''-----------------------------------------------------------------------------------------------------------------------
In questa sezione sono contenute le funzioni di test. Tali funzioni ricevono un parametro in input, chiamato "samples".
Tale parametro definisce il numero di campioni su cui effettuare le varie simulazioni. 
Si effettuano simulazioni per grafi dotati di un numero di nodi da 1 sino a samples*samples'''

def testGenerateGraph(samples):
    testArray = [None] * samples
    timeArray = [None] * samples
    for i in range(0,samples):
        rows = i+1
        columns = i+1
        testArray[i] = rows*columns
        timestamp1 = datetime.timestamp(datetime.now())
        Maze.generateGraph(rows, columns)
        timestamp2 = datetime.timestamp(datetime.now())
        timeArray[i] = timestamp2-timestamp1
    return timeArray

def testKruskal(samples):
    testArray = [None] * samples
    timeArray = [None] * samples
    for i in range(0,samples):
        rows = i+1
        columns = i+1
        testArray[i] = rows*columns
        G = generateGraph(rows, columns)
        timestamp1 = datetime.timestamp(datetime.now())
        Maze.kruskalAlgorithm(G)
        timestamp2 = datetime.timestamp(datetime.now())
        timeArray[i] = timestamp2-timestamp1
    return timeArray

def generateTestArray(samples):
    testArray = [None] * samples
    for i in range(0,samples):
        testArray[i] = (i+1)*(i+1)
    return testArray
'''-------------------------------------------------------------------------------------------------------------'''
'''Sezione dedicata all'esecuzione dei test veri e propri. Nella prima parte viene richiesto all'utente il numero di campioni su cui eseguire i vari test.
Successivamente i test sono eseguiti sulle funzioni "kruskalAlgorithm()" e "generateGraph()".
I risultati dei test sono restituiti in forma grafica, mediante l'ausilio delle primitive offerte dalla libreria Matplotlib.'''
samples = int(input("Inserire il numero di campioni su cui eseguire gli esperimenti: "))
testArray = generateTestArray(samples)
timeArrayKruskal = testKruskal(samples)
timeArrayGenerateGraph = testGenerateGraph(samples)


plt.subplot(2,1,1)
plt.plot(testArray,timeArrayGenerateGraph,'s')
plt.xlabel("Dimensione dell'input (numero di vertici)")
plt.ylabel('Tempo di esecuzione (s)')
plt.plot(testArray,timeArrayGenerateGraph)
plt.title('Funzione di Generazione del grafo')
plt.tight_layout()
plt.grid(True)

plt.subplot(2,1,2)
plt.plot(testArray,timeArrayKruskal,'s')
plt.xlabel("Dimensione dell'input (numero di vertici)")
plt.ylabel('Tempo di esecuzione (s)')
plt.plot(testArray,timeArrayKruskal)
plt.title('Funzione di calcolo del MST')
plt.grid(True)
plt.tight_layout()
plt.show()





