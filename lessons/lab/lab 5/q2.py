"""(q2.py) M/M/c queueing system with monitor"""

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
        arrivetime = now()
        yield request, self, G.server
        t = random.expovariate(mu)
        yield hold, self, t
        yield release, self, G.server
        delay = now()-arrivetime
        G.delaymon.observe(delay)
        print(now(), "Observed delay", delay)

class G:
    server = 'dummy'
    delaymon = 'Monitor'

def model(c, N, lamb, mu, maxtime, rvseed):
    # setup
    initialize()
    random.seed(rvseed)
    G.server = Resource(c)
    G.delaymon = Monitor()
   
    # simulate
    s = Source('Source')
    activate(s, s.run(N, lamb, mu))
    simulate(until=maxtime)
   
    # gather performance measures
    W = G.delaymon.mean()
    return(W)

## Experiment ----------------
result = model(c=1, N=20, lamb=0.96, mu=1.00, maxtime=2000000, rvseed=123)
print("")
print("Estimate of W:", result)
