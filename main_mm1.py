"""Perform simulation of a M/M/1 queueing system using SimPy."""
import simpy
import models.simpy_m_m_1 as simpy_mm1

# Default parameters
ARRIVAL_RATE = 10.0  # Arrival rate (clients per second)
SERVICE_RATE = 50.0  # Service rate (clients per second)
SIM_DURATION = 10_000  # Duration of the simulation (seconds)

def main(arrival_rate=ARRIVAL_RATE, service_rate=SERVICE_RATE, sim_duration=SIM_DURATION):
    """Run the M/M/1 queue simulation.

    The function takes the arrival rate, service duration, and simulation duration as parameters.
    It returns the mean response time and mean number of clients in the system.
    """

    # Create the SimPy environment and the server
    env = simpy.Environment()
    server = simpy.Resource(env, capacity=1)

    # Create the M/M/1 queueing system
    mm1_queue = simpy_mm1.SimpyQueue(env, server, arrival_rate, service_rate)

    # Start the request generator and the statistics recorder
    env.process(mm1_queue.generate_requests())
    env.process(mm1_queue.record_statistics(sampling_interval=1.0))

    # Run the simulation
    env.run(until=sim_duration)

    # Compute and print the statistics
    result = mm1_queue.compute_statistics()
    print(f"Mean response time: {result['E[T]']:.4f} seconds")
    print(f"Mean number of clients in the system: {result['E[N]']:.4f}")
    return result


if __name__ == "__main__":
    main()
