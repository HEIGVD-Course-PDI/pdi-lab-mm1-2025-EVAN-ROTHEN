import simpy
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from  models.simpy_m_m_1 import SimpyQueue
from statistics import mean

def run_sim(arrival_rate, service_rate, sim_duration=5000, sampling_interval=1.0):
    env = simpy.Environment()
    server = simpy.Resource(env, capacity=1)
    q = SimpyQueue(env, server, arrival_rate, service_rate)
    env.process(q.generate_requests())
    env.process(q.record_statistics(sampling_interval=sampling_interval))
    env.run(until=sim_duration)
    return q.compute_statistics()

mu = 50.0
lambdas = np.linspace(1.0, 49.0, 25)
rhos = lambdas / mu
E_T = []
E_N = []

for lam in lambdas:
    r = run_sim(lam, mu, sim_duration=5000)
    E_T.append(r['E[T]'])
    E_N.append(r['E[N]'])

plt.figure()
plt.plot(rhos, E_T)
plt.xlabel('Utilisation ρ (λ/μ)')
plt.ylabel('E[T] (s)')
plt.title('Mean response time vs utilisation')
plt.tight_layout()
plt.savefig('mm1_t.png')

plt.figure()
plt.plot(rhos, E_N)
plt.xlabel('Utilisation ρ (λ/μ)')
plt.ylabel('E[N]')
plt.title('Mean number in system vs utilisation')
plt.tight_layout()
plt.savefig('mm1_n.png')

