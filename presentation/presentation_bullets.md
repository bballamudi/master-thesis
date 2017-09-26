# Deep Feature Extraction for Sample-Efficient Reinforcement Learning

## Introduction
**0.00 - 0.30**

* DRL + definizione
* Cosa abbiamo fatto + motivazione

## Table of Contents
**0.30 - 1.00**

* Tre campi
* Lavoro svolto

## Deep Learning
**1.00 - 2.00**

* Definizione DL 
* Composizione a livelli
* ANN + CNN (con descrizione + tipo di dominio)

## Reinforcement Learning
**2.00 - 3.00**

* MDP + descrizione
* Obiettivo RL
* Definizione Q 
* Q ottima

## Deep Reinforcement Learning
**3.00 - 4.00**

* Definizione DRL
* Videogiochi come ambiente di test
* Descrizione DQN
* Da DQN sono nati molti algoritmi

## Our Algorithm
**4.00 - 5.00**

* Problema: algoritmi di DRL usano 1e6 campioni
* Descrizione procedura: loop, epsilon, tre moduli
* Differenze da alti algoritmi: separare le tre fasi

## Autoencoder
**5.00 - 6.00**

* Definizione AE
* Scopo AE (la prima metà...)
* Compressione da S a S_tilde

## Recursive Feature Selection
**6.00 - 7.00**

* RFS riduce lo spazio a S_cappello
* Scopo di RFS (AE + efficienza)
* Funzionamento RFS
* Riassunto puntando ad albero
* Esempio

## Fitted Q-iteration
**7.00 - 8.00**

* FQI produce Q ottimale, dataset convertito a S_cappello
* Funzionamento FQI (target = TD step)
* Output del modello (con input su S_cappello)

## Final Composition
**8.00 - 9.00**

* Composizione a partire da S (con breve spiegazione)
* Politica ottima

## Experiments
**9.00 - 9.30**

* Tre giochi Atari per confronto con DQN
* Moduli separati + combinazione

## Experiments: AE reconstruction and features
**9.30 - 10.30**

* Fila in alto: precisione
* File in basso: astrazione delle feature

## Experiments: S-Q test
**10.30 - 11.30**

* Verificare adeguatezza delle feature per controllo
* Regressore supervisionato per apprendere Q di DQN da feature
* Stesso input delle reti
* Predizione in validazione: OK

## Experiments: RFS
**11.30 - 12.30**

* Tempi intrattabili e pochi risultati
* Output su Pong OK, ma inconsistente su altri ambienti
* RFS importante per algoritmo, ma tolto da fase sperimentale

## Experiments: FQI samples
**12.30 - 13.30**

* Analisi comparativa: 25% punteggio
* Valutare prestazione in termini di campioni
* Limitare il numero a 100k: 8 volte meglio di DQN

## Experiments: FQI efficiency
**13.30 - 14.30**

* Considerando prestazioni massime algoritmi: 100 volte meno campioni
* Efficienza esplicita: 100 volte più alta
* 25% punteggio, 0.3% campioni
* Obiettivo raggiunto, ma non buona performance assoluta

## Conclusions
**14.30 - 16.00**

* Proseguimento lavoro per aumentare performance
* Estrazione feature per avere più astrazione e dinamiche contenute
* Modificare raccolta dataset per avere più esplorazione
* Pubblicare risultati
 











































