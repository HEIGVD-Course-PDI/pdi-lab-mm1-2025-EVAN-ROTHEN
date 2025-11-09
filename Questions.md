Questions to answer
==================================

These are the questions related to the M/M/1 queueing model using SimPy.

You will need to answer the questions in this file. Your answers will be graded. 

You can answer in English or French.


1-Implement the M/M/1 queueing model in SimPy
---------------------------------------------

### The implementation in the file `models/simpy_m_m_1.py` counts for 4 points maximum. (4p)

```python

"""SimPy simulation of an M/M/1 queueing system.
The system has a single server and an infinite queue.
The inter-arrival time is exponentially distributed (Poisson arrivals).
The service time is exponentially distributed.
"""

from statistics import mean
import numpy as np
# ---------------------------------------------------------------------------
class SimpyQueue:
    """Class representing an M/M/1 queueing system using SimPy."""

    def __init__(self, env, server, arrival_rate, service_rate):
        """Initialize the parameters of the M/M/1 queueing system and the statistics arrays."""
        self.env = env
        self.server = server
        self.interarrival_time = 1.0 / arrival_rate
        self.service_time = 1.0 / service_rate
        # Statistics
        self.response_times = []
        self.clients_in_system = []


    def generate_requests(self):
        """Generate requests following a Poisson process."""
        while True:
            # ******** Add your code here ********
            # intervalle tiré de l'exponentiell
            inter = np.random.exponential(self.interarrival_time)
            yield self.env.timeout(inter)
            # appel d'un processus pour gérer la requête
            self.env.process(self.process_request())


    def process_request(self):
        """Place a request in the queue and process it when the server is available.

        The method also records statistics about the response time.
        """
        arrival_time = self.env.now

        # ******** Add your code here ********

        with self.server.request() as req:
            yield req
            # temps de service exp avec rate = service_rate
            serv = np.random.exponential(self.service_time)
            yield self.env.timeout(serv)

        departure_time = self.env.now
        self.response_times.append(departure_time - arrival_time)


    def record_statistics(self, sampling_interval):
        """Periodically collect statistics about the number of clients in the system."""
        while True:
            yield self.env.timeout(sampling_interval)
            self.clients_in_system.append(self.server.count + len(self.server.queue))


    def compute_statistics(self):
        """Compute and return the mean response time and mean number of clients in the system."""
        mean_response_time = mean(self.response_times)
        mean_clients_in_system = mean(self.clients_in_system)
        return {'E[T]': mean_response_time, 'E[N]': mean_clients_in_system}

```


2-Validate the simulation model
-------------------------------

#### Show at least 3 different simulation results with different parameters and compare them with the analytical model. (6p)

A = Arrival rate
S = Server rate

##### Cas 1 
- A = 10, S = 50
- ρ = 10 / 50 = 0.20  
- Valeurs analytiques : E[T] = 1/(50−10) = 0.02500 s, E[N] = 0.25  
- Résultat simulation :  
```text
   Mean response time: 0.0249 s  
   Mean number in system: 0.2455  
```
- Erreurs relatives :  
  - E[T] : (0.0249 − 0.02500) / 0.02500 = −0.40%  
  - E[N] : (0.2455 − 0.25) / 0.25 = −1.80%
- Commentaire : excellent accord. Variations résiduelles attendues

##### Cas 2 
- A = 30, S = 50
- ρ = 30 / 50 = 0.60  
- Valeurs analytiques : E[T] = 1/(50−30) = 0.05000 s, E[N] = 1.5  
- Résultat simulation :  
  ```text
  Mean response time: 0.0495 s  
  Mean number in system: 1.5009  
  ```
- Erreurs relatives :  
  - E[T] : (0.0495 − 0.05000) / 0.05000 = −1.00% 
  - E[N] : (1.5009 − 1.5) / 1.5 = +0.06%
- Commentaire : accord très bon.

##### Cas 3 
- A = 50, S = 50 
- ρ = 50 / 50 = 1.0  
- Formules analytiques : E[T] et E[N] divergent (→ ∞). Le modèle M/M/1 est instable quand λ ≥ μ.  
- Résultat simulation :
```text  
  Mean response time: 7.3308 s  
  Mean number in system: 366.1903  
```
- Explication : la simulation retourne des valeurs finies car :
  - la simulation est de durée finie (`SIM_DURATION`),  
  - l’échantillon est fini et la file croît fortement avant la fin.  
  Ces valeurs sont un symptôme d’instabilité. Si on augmente la durée on verra la moyenne continuer à croître ou une variance énorme.  


3-Evaluate the impact of an load increase
-----------------------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 30/s` and `SERVICE_RATE = 50/s`? (2p)

```text
Mean response time: 0.0502 seconds
Mean number of clients in the system: 1.4869
```

#### What are the simulation results when running with a 40% increased `ARRIVAL_RATE`? (2p)

```text
Mean response time: 0.1260 seconds
Mean number of clients in the system: 5.3299
```

#### Interpret and explain the results. (3p)

Augmenter λ de 30 à 42 (+40%) augmente fortement ρ (0.6 à 0.84). 
Le système passe d'une zone de charge modérée à une charge très élevée.
E[T] augmente de 0.05 s à 0.125 s (x2.5)
E[N] augmente beaucoup plus (1.5 → 5.25, x3.5)
Proche de la capacité, des petites augmentations de charge provoquent des augmentations non linéaires des délais et de l'encombrement


4-Doubling the arrival rate
---------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 40/s` and `SERVICE_RATE = 50/s`? What is the utilization of the server? (2p)

```text

Mean response time: 0.0979 seconds
Mean number of clients in the system: 3.9060

```

A = 40/50 = 0.8
E[T] = 1/(50-40) = 1/10 = 0.1s
E[N] = 0.8/0.2 = 4

#### What is the value of `SERVICE_RATE` that achieves the same mean response time when doubling the `ARRIVAL_RATE` to `80/s`? What is the server utilization in that case? (2p)

S = Service rate
A = Arrival rate

On veut 1/(S − 80) = 0.1.
Calcul détaillé : 1/(S − 80) = 0.1 ⇒ S − 80 = 1/0.1 = 10 ⇒ μ = 90.
Donc SERVICE_RATE = 90/s.
Utilisation dans ce cas : p = 80 / 90 = 8/9 ≈ 0.888888... ≈ 0.8889.
E[N] analytique = p / (1 − p) = (8/9) / (1/9) = 8

```text

Mean response time: 0.1013 seconds
Mean number of clients in the system: 8.1673

```

#### Use the analytical M/M/1 model to confirm your findings. (3p)

- arrivées selon un processus de Poisson
- temps de service exponentiels
- 1 seul serveur
- une file d'attente infinie 

les formules E[T] = 1/(S-A) et E[N]=p/(1-p) confirment les résultats ci-dessus. Doubler A obligera à augementer S de plus de x2 pour garder le même E[T]

#### Describe and interpret the results. (3p)

Pour maintenir la même latence quand la charge double, il faut augmenter la capacité de service de plus de 100% si la capacité de base était proche du point de saturation. Le taux d'utilisation augmente et le nombre moyen de clients aussi


5-Rule of Bertsekas and Gallager
--------------------------------

#### Describe your experiments and results. (2p)

on choisit A0 et S0. executé deux deux simulation : (A0,S0) et (k*A0,k*S0). Puis comparer E[T]

#### Provide an analytical explanation of your findings. (2p)

E[T]_0 = 1/(S0-A0)
E[T]_k = 1/(k*S0-k*A0) = 1(k*(S0-A0)) ) 1/k * E[T]_0

Donc la règle tient de manière analytique pour M/M/1. Si on multiplie à la fois A et S par k. La latence moyenne se réduit exactement par k. 


Conclusion
----------

#### Document your conclusions here. What did you learn in this lab? (2p)

En conclusion les formules analytiques M/M/1 sont simples et prédictives, quand p s'approche de 1, E[T] et E[N] explosent non linéairement. Une petite augmentation de A produit un allongement conséquent des délais. Pour garder la même latence quand on double la charge, il faut augmenter S de plus de 100% avec des calculs bien sûr. La règle de Bertsekas & Gallager est validée analytiquement pour M/M/1, si on multiplie S et A par k, E[T] est divisé par k
