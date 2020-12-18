#!/usr/bin/python3
# 2D Ising model program
# This material is released under a Creative Commons License
# (Attribution-Noncommercial-Share Alike License)
# (http://creativecommons.org/licenses/by-nc-sa/3.0/) 
# with the following attribution:
# "Original version of this material was developed by 
# Prof. Michael Colvin at UC Merced"

import random
import math
import sys

ntimes=10000     # Time steps per run
nequil=1000      # Equilibration steps
#n=10             # Sites per edge for n x n system
#Temp=1.0         # Default Temperature

# If one argument is given, set the temperature to that
if (len(sys.argv)<3):
    sys.exit("Usage: Ising_model.py [Temperature (10-100)] [N (3-20)], e.g. Ising_model.py 25 8")

Temp=float(sys.argv[1])/10.0 
n=int(sys.argv[2]) 

# Set some useful values
n2=n*n
n4=n2*n2
nflips=8*n*n     # Spin flips per time step

# Initialize sums for averages
E_sum=0.0
E2_sum=0.0
M_sum=0.0
M2_sum=0.0

# Matrix of spins
spins=[]
for i in range(n):
    spins.append([])
    for j in range(n):
        spin=1
        if (random.random() < 0.5):
            spin=-1
        spins[i].append(spin)

# Run simulation
for timestep in range(ntimes+nequil):
    for flip in range(nflips):
        # Randomly pick a site
        i=int(n*random.random())
        j=int(n*random.random())

        #Calculate the change in energy if we flip this spin
        deltaE=(-2./Temp)*spins[i][j]*\
            (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
             spins[(i+1)%n][j]+spins[(i+n-1)%n][j])

        #Flip the spin using Metropolis MC
        if (math.exp(deltaE)>random.random()):   
                spins[i][j]=-spins[i][j]
                
    # End of loop over spins
    # Calculate system energy and magnetism
    if (timestep > nequil):
        energy=0.0  
        magnetism=0.0
        for i in range(0,n):
            for j in range(0,n):
                energy-=spins[i][j]*\
                    (spins[i][(j+1)%n]+spins[i][(j-1+n)%n]+\
                     spins[(i+1)%n][j]+spins[(i+n-1)%n][j])
                magnetism+=spins[i][j]

        E_sum+=energy/n2
        E2_sum+=energy*energy/n4
        M_sum+=abs(magnetism)/n2
        M2_sum+=magnetism*magnetism/n4

E_ave=E_sum/(ntimes)
M_ave=M_sum/(ntimes)
E_sd=math.sqrt((E2_sum-E_sum*E_sum/ntimes)/(ntimes-1))
M_sd=math.sqrt((M2_sum-M_sum*M_sum/ntimes)/(ntimes-1))
print('%8.4f %10.4f %10.4f %10.4f %10.4f'%(Temp, E_ave, E_sd, M_ave, M_sd))
