# Master's Thesis - Daniele Grattarola

This repo contains the Latex source code and additional files required to 
build my Master's thesis and output it as PDF. 

## Abstract
Deep reinforcement learning (DRL) has been under the spotlight of artificial intelligence research in recent years, enabling reinforcement learning agents to solve control problems that were previously considered intractable. The most effective DRL methods, however, require a great amount of training samples (in the order of tens of millions) in order to learn good policies even on simple environments, making them a poor choice in real-world situations where the collection of samples is expensive.  
In this work, we propose a sample-efficient DRL algorithm that combines unsupervised deep learning to extract a representation of the environment, and batch reinforcement learning to learn a control policy using this new state space. We also add an intermediate step of feature selection on the extracted representation in order to reduce the computational requirements of our agent to the minimum. We test our algorithm on the Atari games environments, and compare the performance of our agent to that of the DQN algorithm by Mnih et al. (2015). We show that even if the final performance of our agent amounts to a quarter of DQN’s, we are able to achieve good sample efficiency and a better performance on small datasets

## Building the PDF
To build, simply run the following in a terminal:
```sh
git clone https://github.com/danielegrattarola/master-thesis.git
cd master-thesis
make
make clean
```

If you have Evince (default PDF reader of Ubuntu) installed on your system, the 
PDF will automatically open. Otherwise, you can find it at ```master-thesis/thesis.pdf```.



