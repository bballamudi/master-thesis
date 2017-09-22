# Deep Feature Extraction for Sample-Efficient Reinforcement Learning

## Introduction
**30 seconds**

* General context: AI, RL, DRL (= RL with deep representations)
* Our algorithm: separate extraction and policy learning, goal is efficiency

Buongiorno. 
Il lavoro che presento oggi si colloca nel campo del deep reinforcement learning, 
ovvero quegli algoritmi di apprendimeno per rinforzo che utilizzano in qualche 
modo approssimatori profondi. 

Abbiamo lavorato a un algoritmo modulare, che combina l'apprendimento profondo 
e non supervisionato con un algoritmo classico di reinforcement learning, con
lo scopo di diminuire il più possibile il numero di campioni di addestramento 
che utilizziamo; quindi il nostro obiettivo è stato aumentare l'efficienza, 
rispetto ad algoritmi molto potenti, ma molto poco efficienti.

## Table of Contents
**30 seconds**

Nelle prossime slide parleremo dei campi principali che andiamo a trattare 
(D, R, e DR learning), e poi andrò nei dettagli del lavoro svolto. 

## Deep Learning
1 minute

 * Learn a representation of the domain
* Hierarchical composition of simple but nonlinear modules
* Neural networks: parametric model, gradient descent
* Convolutional neural networks

Il deep learning è una branca del machine learning per apprendere una 
rappresentazione astratta di un dominio. 

I modelli profondi sono composti a livelli (come vedete qui), in cui ogni livello 
trasforma ulteriormente la rappresentazione del livello precedente, a partire 
dal dominio, fino a che questa rappresentazione viene poi usata per risolvere 
problemi di ML (classificazione, regressione...). 
Il modello deep più noto sono le reti neurali, ispirate al cervello biologico, e 
in particolare noi abbiamo usato le reti neurali convoluzionali, 
che utilizzano dei filtri che vengono fatti scorrere sul dominio per estrarre
correlazioni spaziali (tipicamente vengono applicate a immagini o a domini 
strutturati di questo tipo).

## Reinforcement Learning
1 minute

Allo stesso tempo, parliamo di reinforcement learning. Rappresentiamo il 
problema come un processo decisionale di Markov, con un agente che sceglie delle
azioni e un ambiente che restituisce un'osservazione e un rinforzo.

In RL l'obiettivo è individuare una politica ottima, che massimizzi la somma di 
questo rinforzo (il ritorno atteso).

L'unico concetto fondamentale che vediamo è quello di valore di azione (la 
funzione Q), che ci dice, quanto vale scegliere un'azione in uno stato, 
in termini di ritorno atteso, dato che l'agente sta seguendo una politica.
Possiamo parlare anche di Q ottima, associata alla politica ottima, e 
tipicamente si va ad approssimare questa funzione per poi utilizzarla nel 
controllo (come vedremo dopo).


## Deep Reinforcement Learning
1 minute

* RL algorithms that use deep representations
* DQN, AlphaGo, NEC

Arriviamo al deep reinforcement learning, ovvero algoritmi di reinforcement 
learning che utilizzano modelli deep per rappresentare l'ambiente. 
Algoritmi di deep reinforcement learning noti, sono innanzittutto l'algoritmo 
DQN (con cui poi andremo a confrontarci in quanto è la baseline del DRL) che 
utilizza una rete neurale convoluzionale per apprendere la funzione Q ottima a 
partire dalle immagini dell'ambiente, oppure architetture più complesse come 
AlphaGo, che di recente ha sconfitto per la prima volta nella storia 
tutti i migliori giocatori di Go.
Un altro algoritmo importante è neural episodic control, che utilizza delle 
strutture di memoria per migliorare la convergenza di DQN.

## Our Algorithm
**5 minutes**

E proprio su questo tema, abbiamo impostato il nostro algoritmo. 
Lo scopo di questo lavoro è stato ottimizzare il numero di campioni necessari
a convergere, cercando di ridurli rispetto alle decine di milioni necessari
ai migliori algoritmi che ho appena citato.

Dunque abbiamo lavorato a questa procedura, composta da un loop esterno che 
parte dalla raccolta di un training set di transizioni dell'ambiente, e utilizza 
questi campioni per addestrare tre moduli separati (li vedete qui): un modulo
di estrazione di feature dall'ambiente (a partire dalle immagini), un modulo che
ottimizza lo spazio estratto ai fini del controllo, e abbiamo poi un algoritmo 
di reinforcement learning che approssima la Q ottimale. 

Aver separato le tre fasi è ciò che ci differenzia dagli altri algoritmi di DRL. 

Partiamo da un'esplorazione random, e ad ogni step dell'algoritmo andiamo ad 
abbassare il tasso di esplorazione per raccogliere il dataset e utilizziamo 
sempre di più la conoscenza appresa, fino a convergenza.

I tre moduli che addestriamo sono i seguenti.
Per l'estrazione delle feature usiamo un autoencoder convoluzionale, quindi una
rete neurale che addestriamo in maniera non supervisionata a predire il proprio
input (in questo caso l'input sono 4 osservazioni successive dell'ambiente, come
per DQN), e lo scopo dell'autoencoder è che la prima metà della rete estragga
una rappresentazione compressa e sparsa dello spazio di ingresso, ma che 
contenga sufficiente informazione affinchè la seconda metà della rete possa 
ricostruire i 4 frame originali.
Quindi noi andiamo a comprimere lo spazio di ingresso, in questa trasformazione
dallo spazio delle immagini allo spazio delle feature.

Questo spazio viene poi passato in ingresso all'algoritmo di Recursive Feature
Selection (RFS), che è un algoritmo di selezione delle feature orientato a 
ridurre lo spazio di stato-azione di un problema di reinforcement learning,
tenendo solo quelle feature che sono maggiormente utili al controllo.
Lo scopo di questa fase è migliorare i tempi computazionali dell'agente stesso, 
rimuovendo dalla rappresentazione ciò che non è necessario.
In prima battuta, l'algoritmo utilizza un modello supervisionato per andare
a stimare quali feature di stato e azione speighino la maggior quantità di 
varianza nel segnale di rinforzo, e scartando quelle meno importanti; dopodichè
lo stesso procedimento viene applicato in maniera ricorsiva, tenendo solo quelle
feature che spiegano meglio la varianza delle feature di stato selezionate. 
Si crea dunque una sorta di albero (come vedete qui), che parte dallo spiegare
il rinforzo e termina quando non vengono più aggiunte feature. 
In questo caso la y non serve a spiegare la dinamica del rinforzo che è 
uguale per ogni y, e non serve a spiegare la dinamica della x, perchè abbiamo 
un'azione dedicata.

Il terzo e ultimo modulo che addestriamo è l'algoritmo fitted Q-iteration (FQI), 
un algoritmo batch, che lavora su un dataset costante, e che va ad approssimare
la Q ottimale dell'ambiente. 
L'algoritmo funziona in maniera iterativa, e ad ogni step va ad addestrare un 
modello supervisionato integrando nel target uno step di temporal difference
utilizzando la precedente approssimazione della Q-function (più il rinforzo).
Notare che l'input del modello è sullo spazio di feature estratto e ridotto, 
e che andiamo a produrre un'approssimazione della Q ottima su questo spazio. 

Una volta ottenuta questa approssimazione della Q, andiamo a comporre i tre
moduli, in modo da produrre un'approssimatore della Q ottimale a partire
dallo spazio degli stati originale. Quindi a partire dalle immagini, estraiamo
le feature, riduciamo lo spazio, e calcoliamo la Q (usando anche le azioni).
A questo punto otteniamo un'approssimazione della politica ottima, scegliendo in
ogni stato l'azione che massimizza la Q ottimale, perchè per definizione 
andrà a massimizzare il ritorno atteso.
E dunque questo è il nosto agente.

## Experiments
**5 minutes**

Abbiamo testato il nostro algoritmo su tre giochi Atari per confrontarlo 
direttamente con DQN.
Abbiamo condotto esperimenti sui vari moduli separatamente e poi sulla 
combinazione finale.

Partendo dall'autoencoder, in questa slide vediamo due cose: 
    - nella fila in alto, vediamo come l'autoencoder sia in grado di ricostruire
    l'ingresso (un campione sono 4 frame consecutivi, e quindi anche la 
    ricostruzione avviene su 4 frame; qui vediamo le rispettive coppie di frame,
    ingresso-ricostruzione) e vediamo che la rete ha una precisione molto alta
    praticamente il 100%.
    - nella fila in basso, invece, vediamo il valore delle feature (cioò che 
    viene prodotto dall'encoder) e, oltre ad essere interessante da vedere, ci
    è servito per valutare il livello di astrazione (che è abbastanza buono; 
    ci sono dei casi in cui le feature sono semplicemente una compressione 
    delle immagini, qui invece c'è astrazione)

Sempre in tema feature, abbiamo voluto verificare quanto le feature fossero
adatte ad apprendere la Q con FQI. 
Per fare ciò abbiamo addestrato un modello supervisionato, che a partire
dalle feature approssimasse la stessa Q appresa da DQN (quindi usavamo le 
feature come dominio e la Q di DQN come target). Questa cosa si è potuta fare
perchè le due reti prendono praticamente lo stesso ingresso. 
E i risultati hanno confermato la qualità delle feature: questa è una predizione 
in validazione, abbiamo i valori reali e predetti (che dovrebbero essere uguali)
e l'R2 della predizione è molto alto.

Parliamo anche di RFS.
Purtroppo ci siamo scontrati con dei tempi computazionali intrattabili, 
e abbiamo ottenuto pochi risultati sperimentali ma su cui non abbiamo potuto 
eseguire un'analisi approfondita.
Qui vedete la selezione delle feature su Pong (circa un terzo delle feature 
vengono selezionate), ma negli altri casi vengono selezionate tutte le feature
o nessuna feature, senza consistenza. 
Abbiamo comunque scelto di lasciare RFS nella tesi, perchè è sicuramente
fondamentale per spazi più complessi di quelli che stiamo vedendo ora, ma
l'abbiamo tolto dalla pipeline per rendere trattabili gli esperimenti 
più importanti, di cui vado a parlare ora. 

Esperimenti più importanti e interessanti, invece, che riguardano 
l'apprendimento della politica.

Qui vediamo un'analisi comparativa del nosto algoritmo con una politica random
e la politica ottima appresa da DQN, sui tre ambienti. 
Vediamo come il nostro agente si collochi in mezzo fra i due, riusciamo in media
a raggiungere il 25% dei punteggi di DQN; ma, poichè il nostro obiettivo era
quello di aumentare l'efficienza, abbiamo valutato le prestazioni considerando
il numero di campioni utilizzati. 
La prima considerazione è stata quella di limitare il training set a 100k 
campioni (quelli che servono al nostro algoritmo per raggiungere il suo massimo).
E, con 100k campioni, vediamo che il nostro agente fa in media 8 volte più punti
di DQN, che a volte non riesce nemmeno a superare il random.

Ma anche considerando le prestazioni massime degli algoritmi, andando a 
valutare il numero di campioni di addestramento, vediamo che il nostro agente
utilizza 100 volte meno campioni di DQN. 
E, da questa considerazione, noi possiamo anche calcolare esplicitamente 
l'efficienza dei due algoritmi, in termini di reward per campione, e vediamo
che il nostro algoritmo è 100 volte più efficiente, quindi raggiungiamo sì
il 25% di DQN ma con 0,3% dei campioni in media.
Quindi, l'obiettivo di efficienza è sicuramente raggiunto, anche se l'algoritmo
non riesce ad avere una buona performance assoluta. 

## Conclusion
**1 minute**

In questi termini stiamo proseguendo il lavoro. Al momento stiamo lavorando 
all'estrazione di feature, per saturare il più possibile le prestazioni 
dell'algoritmo, e l'altro aspetto importante sarà di lavorare al tasso di 
esplorazione; perchè FQI necessita di una buona varietà di campioni nel training
set, per avere stati a valore alto e a valore basso, quindi stiamo pensando di
modificare la raccolta semi-batch, in maniera più simile a una replay memory
da cui campionare i sample.
Quindi questo è tutto, spero di non avervi annoiato e grazie per l'attenzione. 
 











































