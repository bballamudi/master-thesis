# Deep Feature Extraction for Sample-Efficient Reinforcement Learning

## Introduction
**0.00 - 0.30**

Buongiorno.

Il lavoro che presento oggi si colloca nel campo del deep reinforcement learning, 
ovvero l'utilizzo di approssimatori profondi in algoritmi di apprendimento
per rinforzo.  

Abbiamo lavorato a un algoritmo modulare, con lo scopo di aumentare l'efficienza
nell'utilizzo dei campioni di addestramento, rispetto ad algoritmi dello stato
dell'arte, molto potenti, ma molto poco efficienti.

## Table of Contents
**0.30 - 1.00**

Nelle prossime slide parleremo dei campi principali che andiamo a trattare 
(D, R, e DR learning), e poi andrò nei dettagli del lavoro svolto. 

## Deep Learning
**1.00 - 2.00**

Il deep learning è una branca del machine learning per apprendere una 
rappresentazione astratta di un dominio. 

I modelli profondi sono composti a livelli (come vedete qui), in cui ogni livello 
trasforma ulteriormente la rappresentazione del livello precedente, a partire 
dal dominio, fino a che questa rappresentazione viene poi usata per risolvere 
problemi di ML (classificazione, regressione...). 

Il modello deep più noto sono le reti neurali, ispirate al cervello biologico, e 
in particolare noi abbiamo usato le reti neurali convoluzionali, che utilizzano 
dei filtri che vengono fatti scorrere sul dominio per estrarre correlazioni 
di tipo spaziale (tipicamente vengono applicate a immagini o a domini 
strutturati di questo tipo, noi le applicheremo ad immagini).

## Reinforcement Learning
**2.00 - 3.00**

Allo stesso tempo, parliamo di reinforcement learning. Rappresentiamo il 
problema come un processo decisionale di Markov, con un agente che sceglie delle
azioni e un ambiente che restituisce un'osservazione e un rinforzo.  

In RL l'obiettivo è individuare una politica ottima, che massimizzi la somma di 
questo rinforzo (il ritorno atteso).

L'unico concetto fondamentale che vediamo è quello di valore di azione (la 
funzione Q), che ci dice, quanto vale scegliere un'azione in uno stato, 
in termini di ritorno atteso, dato che l'agente sta seguendo una certa politica.  

Possiamo parlare anche di Q ottima, associata alla politica ottima, e 
tipicamente si va ad apprendere questa funzione per poi utilizzarla nel 
controllo (come vedremo dopo).


## Deep Reinforcement Learning
**3.00 - 4.00**

Arriviamo al deep reinforcement learning, ovvero algoritmi di reinforcement 
learning che utilizzano modelli deep per rappresentare l'ambiente, 
tipicamente a partire dalle immagini. 

Un buon ambiente di test per il DRL sono i videogiochi (con i giochi Atari, che 
poi vedremo), per simulare meglio l'apprendimento umano, che spesso parte da una
rappresentazione visiva.  
 
Nella tesi ci siamo confrontati con l'algoritmo deep Q-learning,
che utilizza una rete neurale convoluzionale chiamata DQN (e spesso ci si 
riferisce così all'algoritmo) per apprendere la funzione Q ottima dell'ambiente 
a partire dalle immagini, e da cui è praticamente rinato il campo del DRL con
una significativa quantità di algoritmi.

## Our Algorithm
**4.00 - 5.00**

Algoritmi che però hanno in comune la necessità di usare decine di milioni
di campioni di addestramento per convergere. E il nostro lavoro si è concentrato
su questo aspetto.

Abbiamo lavorato a questa procedura, composta da un loop esterno che parte dalla
raccolta di un training set di transizioni dell'ambiente, utilizzando un tasso 
di esplorazione decrescente ad ogni step (per sfruttare sempre di più la 
conoscenza appresa), e questi campioni servono ad addestrare tre moduli separati
(li vedete qui): 

* un modello deep per rappresentare l'ambiente
* un modulo che ottimizza lo spazio estratto ai fini del controllo
* e abbiamo poi un algoritmo di reinforcement learning che approssima la Q 
ottimale. 

Aver separato le tre fasi è ciò che ci differenzia dagli altri algoritmi di DRL 
e ci dà un vantaggio in termini di efficienza. 

I tre moduli che addestriamo sono i seguenti.

## Autoencoder
**5.00 - 6.00**

Per l'estrazione delle feature usiamo un autoencoder convoluzionale, quindi una
rete neurale che addestriamo in maniera non supervisionata a predire il proprio
input (in questo caso l'input sono 4 osservazioni successive dell'ambiente, come
per DQN), e lo scopo dell'autoencoder è che la prima metà della rete estragga
una rappresentazione compressa e sparsa dello spazio di ingresso, ma che 
contenga sufficiente informazione affinchè la seconda metà della rete possa 
ricostruire i 4 frame originali.  

Quindi noi andiamo a comprimere lo spazio di ingresso, in questa trasformazione
dallo spazio delle immagini allo spazio delle feature.

## Recursive Feature Selection
**6.00 - 7.00**

Questo spazio viene poi passato in ingresso all'algoritmo di Recursive Feature
Selection (RFS), che riduce lo spazio delle feature in questo spazio S cappello.

Lo scopo di questa fase è ridurre la rappresentazione che l'encoder deve 
computare e, semplificando lo spazio, diminuire il numero di campioni necessari
ad apprendere una politica.  

In prima battuta, l'algoritmo utilizza un modello supervisionato per andare
a stimare quali feature di stato e azione speighino la maggior quantità di 
varianza nel segnale di rinforzo, e scarta quelle meno importanti.  
Dopodichè lo stesso procedimento viene applicato in maniera ricorsiva, andando
via via a spiegare le feature di stato già selezionate.

Si crea dunque una sorta di albero (come vedete qui), in cui si parte dallo 
spiegare il rinforzo e si termina quando non vengono più aggiunte feature.

Vediamo un esempio.  
In questo caso la y non serve a spiegare la dinamica del rinforzo (che è 
uguale per ogni y), e non serve a spiegare la dinamica della x, perchè abbiamo 
un'azione dedicata: e quindi viene scartata.

## Fitted Q-iteration
**7.00 - 8.00**

Il terzo e ultimo modulo che addestriamo è l'algoritmo Fitted Q-iteration (FQI), 
che va ad approssimare la Q ottimale dell'ambiente, usando il dataset convertito
nello spazio delle feature ridotto.  

L'algoritmo funziona in maniera iterativa, e ad ogni step va ad addestrare un 
modello supervisionato integrando nel target uno step simile allo step di 
temporal difference utilizzando la precedente approssimazione della Q-function,
più un termine con il rinforzo.  

L'input del modello è sullo spazio di feature estratto e ridotto, 
e andiamo a produrre un'approssimazione della Q ottima su questo spazio. 

## Final Composition
**8.00 - 9.00**

Una volta ottenuta questa approssimazione della Q, andiamo a comporre i tre
moduli, in modo da produrre un'approssimatore della Q ottimale a partire
dallo spazio degli stati originale.  
Quindi a partire dalle immagini, estraiamo le feature, riduciamo lo spazio, e 
calcoliamo la Q.

A questo punto otteniamo un'approssimazione della politica ottima, scegliendo in
ogni stato l'azione che massimizza la Q ottimale, perchè per definizione 
andrà a massimizzare il ritorno atteso.

E dunque questo è il nosto agente.

## Experiments
**9.00 - 9.30**

Abbiamo testato il nostro algoritmo su tre giochi Atari per confrontarlo 
direttamente con DQN.  
Abbiamo condotto esperimenti sui vari moduli separatamente e poi sulla 
combinazione finale.

## Experiments: AE reconstruction and features
**9.30 - 10.30**

Partendo dall'autoencoder, in questa slide vediamo due cose: 

* nella fila in alto, vediamo come l'autoencoder sia in grado di ricostruire
l'ingresso (un campione sono 4 frame e quindi vediamo le rispettive coppie 
di ingresso-ricostruzione) e vediamo che la rete ha una precisione quasi
del 100%.
* nella fila in basso, invece, vediamo il comportamento delle feature e, 
oltre ad essere interessante da vedere, ci è servito per valutare il livello 
di astrazione (che è abbastanza buono; ci sono dei casi in cui le feature sono 
semplicemente una compressione delle immagini, qui invece c'è astrazione)

## Experiments: S-Q test
**10.30 - 11.30**

Sempre in tema feature, abbiamo voluto verificare quanto le feature fossero
adatte ad apprendere la Q con FQI.  

Per fare ciò abbiamo addestrato un modello supervisionato, che a partire
dalle feature approssimasse la stessa Q appresa da DQN (quindi usavamo le 
feature come dominio e la Q di DQN come target). Da notar che enrambe le reti 
prendono praticamente lo stesso ingresso.  

E i risultati hanno confermato la qualità delle feature: questa è una predizione 
in validazione, abbiamo i valori reali e predetti (che dovrebbero essere uguali)
e vediamo che l'R2 in predizione è molto alto.

## Experiments: RFS
**11.30 - 12.30**

Parliamo anche di RFS.  
Purtroppo ci siamo scontrati con dei tempi computazionali intrattabili, 
e abbiamo ottenuto pochi risultati sperimentali, su cui non abbiamo potuto 
eseguire un'analisi approfondita.  

Qui vedete la selezione delle feature su Pong (circa un terzo delle feature 
vengono selezionate), ma negli altri casi vengono selezionate tutte le feature
o nessuna feature, senza consistenza.   

Abbiamo comunque scelto di lasciare RFS nella tesi, perchè è sicuramente
fondamentale per spazi più complessi di quelli che stiamo vedendo ora, ma
l'abbiamo tolto dalla pipeline per rendere trattabili gli esperimenti 
più importanti, di cui vado a parlare ora. 

## Experiments: FQI score
**12.30 - 13.30**

Esperimenti più importanti e interessanti che riguardano l'apprendimento della 
politica.

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

## Experiments: FQI efficiency
**13.30 - 14.30**

Ma anche considerando le prestazioni massime degli algoritmi, andando a 
valutare il numero di campioni di addestramento, vediamo che il nostro agente
utilizza 100 volte meno campioni di DQN.  

E, da questa considerazione, noi possiamo anche calcolare esplicitamente 
l'efficienza dei due algoritmi, in termini di reward per campione, e vediamo
che il nostro algoritmo è 100 volte più efficiente, quindi raggiungiamo sì
il 25% di DQN ma con lo 0,3% dei campioni in media.  

Quindi, l'obiettivo di efficienza è sicuramente raggiunto, anche se l'algoritmo
non riesce ad avere una buona performance assoluta. 

## Conclusions
**14.30 - 16.00**

In questi termini stiamo proseguendo il lavoro. Al momento stiamo lavorando 
all'estrazione di feature, per saturare il più possibile le prestazioni 
dell'algoritmo, e l'altro aspetto importante sarà quello legato al tasso di 
esplorazione, perchè FQI necessita di una buona varietà di campioni nel training
set, per avere stati a valore alto e a valore basso; quindi stiamo pensando di
modificare la raccolta semi-batch, in maniera più simile a una replay memory
da cui campionare i sample.  
Quindi questo è tutto, spero di non avervi annoiato e grazie per l'attenzione. 
 











































