"""(q1.py) M/M/c queueing system"""

from SimPy.Simulation import *
import random

## Model ----------
class Source(Process):
    """generate random arrivals"""
    def run(self, N, lamb, mu):
        for i in range(N):
            a = Arrival(str(i))
            activate(a, a.run(mu))
            t = random.expovariate(lamb)
            yield hold, self, t

class Arrival(Process):
    """an arrival"""
    def run(self, mu):
        print(now(), "Event: Customer arrives, joins queue")
        yield request, self, G.server
        t = random.expovariate(mu)
        print(now(), "Event: Customer begins service")
        yield hold, self, t
        yield release, self, G.server
        print(now(), "Event: Customer leaves")

class G:
    server = 'dummy'

def model(c, N, lamb, mu, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = Resource(c)
    
    # simulation run
    s = Source('Source')
    activate(s, s.run(N, lamb, mu))
    simulate(until=maxtime)

## Experiment ----------
model(c=1, N=10, lamb=5, mu=2, maxtime=1000000, rvseed=123)
