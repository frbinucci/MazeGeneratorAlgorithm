# MazeGeneratorAlgorithm
##NOTE PRELIMINARI

Il programma realizzato si avvale delle librerie ***Networkx***, ***Matplotlib*** e ***Numpy*** di Python. Se esse non dovessero essere installate occorre installarle mediante i comandi:

1. pip install networkx.
2. pip install matplotlib.
3. pip install numpy.

Se le tre librerie dovessero essere già installate e configurate non si dovrebbero avere problemi nell'esecuzione dei vari script.

##ESECUZIONE DEL SOFTWARE

Se si vuole eseguire il programma e verificare la generazione di diversi labirinti occorre eseguire tramite terminale lo script denominato "mga.py". 
Quest'ultimo richiede preliminarmente quanti labirinti si vogliono generare: per ogni labirinto occorre indicare larghezza, altezza e colori. I labirinti generati vengono presentati di volta in volta all'utente e la loro visualizzazione viene terminata dalla generazione del labirinto successivo.

Se si vuole tenere traccia dei labirinti creati è possibile salvarli come immagini tramite l'apposito pulsante messo a disposizione dalla finestra grafica.

##ESECUZIONE DEI TEST

Se si ha necessità di dover eseguire degli appositi test per la misurazione dei tempi di esecuzione è possibile avvalersi dello script "test.py".
Tale script richiede il numero di test che si vogliono eseguire sulle funzioni 'generateGraph()' e 'kruskalAlgorithm()'. 
Al termine delle varie misurazioni lo script presenta all'utente un grafico in cui è riportato il tempo di esecuzione dei vari algoritmi in funzione della dimensione del grafo su cui operano. 
I risultati delle misurazioni sono memorizzati in una directory denominata "results", sotto forma di file csv. 
Per ogni file viene indicata data e ora del test, nonché l'algoritmo a cui il test fa riferimento. Se non esiste, la cartella 'results' è generata nella medesima locazione in cui si trova lo script di test.