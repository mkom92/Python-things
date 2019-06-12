

# Erlang calculation for the necessary headcount

import math
# import numpy

vol = 100           # Calls
aht = 180           # Average Handle Time seconds
interval = 30       # Minutes
sl = 0.8            # Service Level Agreement target
tt = 60             # Target time
sh = 0.15           # Shrinkage

def Erlang(v,aht,it,sl,tt,sh):

    # Traffic intensity - A
    a = (v*(60/it)*(aht/60))/60

    # Initial number of agents available - N
    n = math.ceil(a) + 1

    ending = 0

    while ending != 1:

         # Probability that a call waits in the queue - p_w
         calc1 = ((a**n)/math.factorial(n))*(n/(n-a))
         calc2 = 0
         for i in range(0, n):
             q = (a**i)/math.factorial(i)
             calc2 += q
         p_w = calc1/(calc1 + calc2)

         if p_w > 1:
             p_w = 1
         elif p_w < 0:
             p_w = 0
         else:
             p_w = p_w

         # SLA calculation
         sla = 1 - (p_w * math.exp(-1*(n-a)*(tt/aht)))

         if sla >= sl:
             ending = 1
         else:
             n += 1

    agents_required = math.ceil(n/(1-sh))
    print("Incoming volume:", v,", AHT:", aht, ", Agents required:", agents_required, ", sla:", "{0:.2%}".format(sla))

Erlang(vol,aht,interval,sl,tt,sh)

'''

mu, sigma = 0, 0.1
s = np.random.normal(mu, sigma, 1000)

'''