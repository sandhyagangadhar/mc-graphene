import numpy as np
from random import random
import matplotlib.pyplot as plt

Nwalker=300;MCSteps=5000
x=[0]*Nwalker
nAccept=0;eSum=0
Lambda=0.2

# Define Building Block Functions
# 1.Initialize function, for setting random walkers' initial positions
# 2.Probability function, allowing acceptance or rejection
# 3.MetropolisStep function,
# 4.oneMonteCarloStep function, performing Nwalker MetopolisSteps

#.......................START.....................
#.................................................

def initialize():

    for i in range(Nwalker):
        x[i]=random()-0.5

def p(xTrial,x):

    # compute the ratio of rho(xTrial) / rho(x)
    return np.exp(-2*Lambda*(xTrial**2-x**2))

def eLocal(x):

    # compute the local energy
    return Lambda + x**2*(0.5-2*Lambda**2)

def MetropolisStep():

    global eSum,nAccept
    # chose a walker at random
    n=int(random()*Nwalker)
    # make a trial move
    delta=0.05*(random()-1)
    xTrial=x[n]+delta

    # Metropolis test
    w=p(xTrial,x[n])

    if w>=random():
        x[n]=xTrial
        nAccept+=1
    # accumulate energy
    e=eLocal(x[n])
    eSum+=e

def oneMonteCarloStep():
    # perform 'Nwalker' Metropolis steps
    for i in range(Nwalker):
        MetropolisStep()

#...............................................
#.....................END.......................


initialize()

# perform 20% of MCSteps as thermalization steps

thermSteps=int(0.2*MCSteps)
print('Performing', thermSteps,'thermalization steps ...')

for i in range(thermSteps):
    oneMonteCarloStep()

# production steps

print('Performing',MCSteps,'production steps ...')
nAccept=0;eSum=0

for i in range(thermSteps):
    oneMonteCarloStep()

# production steps

print('Performing',MCSteps,'production steps ...')
nAccept=0;eSum=0

for i in range(MCSteps):
    oneMonteCarloStep()

# compute and print energy
eAve=eSum/(Nwalker*MCSteps)

print(eAve)
print(nAccept/(Nwalker*MCSteps))