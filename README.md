[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/l6htz_ZV)
Simulation of a M/M/1 queueing system with SimPy
========================================================================


In this lab, we want to use SimPy to simulate a M/M/1 queueing system.

![Single server system](images/queue.svg)

The learning goals of this lab are:

- to learn how simulate a M/M/1 queue with SimPy,
- to apply the analytical M/M/1,
- to understand the behavior of a M/M/1 queueing system when the utilization increases,
- to understand the scaling behavior of a M/M/1 queueing system (load and capacity increase together).


1-Implement the M/M/1 queueing model in SimPy
---------------------------------------------

We first need to implement the M/M/1 queueing model in SimPy. The file `models/simpy_m_m_1.py` provides an incomplete implementation that you have to complete. The model uses a SimPy `Resource` to represent the queueing systems, with a single server (capacity=1).

There also already is a `main` function in the file `./main_mm1.py` that runs the simulation. You can adapt the parameters of the simulation in this file.


2-Validate the simulation model
-------------------------------

Run the simulation model using the `./main_mm1.py` file. You can adapt the parameters of the simulation in this file.
Compare the results of the simulation with the analytical results of the M/M/1 queueing model. You can use the formulas provided in the lecture slides.

#### Todo

- [ ] Answer the questions in the file `Questions.md`.


3-Evaluate the impact of a load increase
-----------------------------------------

To develop an understanding of the behavior of the M/M/1 queueing system, we want to evaluate the impact of an increase of the load on the system.

#### Todo

- [ ] Run the simulation with `ARRIVAL_RATE = 30/s` and `SERVICE_RATE = 50/s`. Note the result.
- [ ] Increase the `ARRIVAL_RATE` by 40% and run the simulation again. Note the result.
- [ ] Answer the questions in the file `Questions.md`.

You should observe that a modest increase of the load can have a significant impact on the performance of the system.


4-Doubling the arrival rate
---------------------------

One of our main questions is: if the arrival rate $\lambda$ doubles, how do we need to increase $\mu$ to achieve the same performance? We will try to answer this question now.


#### Todo

- [ ] Run a simulation with `ARRIVAL_RATE = 40/s` and `SERVICE_RATE = 50/s`. Note the mean response time.
- [ ] Double the `ARRIVAL_RATE` to `80/s`. Using trial and error, find the value of `SERVICE_RATE` that achieves the same mean response time as in the first simulation.
- [ ] Use the analytical M/M/1 model confirm your findings.
- [ ] Answer the questions in the file `Questions.md`.


5-Rule of Bertsekas and Gallager
--------------------------------

In their book "Data Networks", Bertsekas and Gallager provide a rule of thumb for transmission lines:

> *"A transmission line k times as fast will accommodate k times as many packets at k times smaller average delay per packet."*

#### Todo

- [ ] Run an experiment to verify this rule of thumb.
- [ ] Answer the questions in the file `Questions.md`.


6-Plot M/M/1 performance metrics
--------------------------------

Currently, the `main` function in `main_mm1.py` only prints the results of a single simulation. We want to plot the performance metrics (E[T] and E[N] of the M/M/1 queueing system as a function of the utilization $\rho$.

#### Todo

- [ ] Write a script `plot_mm1.py` that runs a series of simulations with increasing utilization $\rho$. Keep $\mu=50/s$ constant and increase $\lambda$ from 0 to almost $\mu$.
- [ ] Generate two plot files: `mm1_t.png` and `mm1_n.png` that show the mean response time E[T] and the mean number of clients in the system E[N] as a function of the utilization $\rho$.


Checklist at the end of the lab
-------------------------------

- [ ] The simulation model `models/simpy_m_m_1.py` is completed and works correctly.
- [ ] You have a script `plot_mm1.py` that runs a series of simulations and generates two plot files.
- [ ] You have the two plot files `mm1_t.png` and `mm1_n.png`.
- [ ] You have answered all the questions in the file `Questions.md`.
