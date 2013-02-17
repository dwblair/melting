from numpy import *
import random
L=250 #system size, compatible with size of display in processing
N=300 #number of particles
r=5 #particle radius
t=0 #time
maxt=1000 #max time
stepSize=r #random step size

#coordinates array
coords=zeros((N,2))+L/2. #start all particles in the center

#print the parameters
#print "#N L r"
#print N,",",L,",",r
#print "#coords"

#run the simulation
for t in range(0,maxt):
    for i in range(0,N):
        x=coords[i][0]
        y=coords[i][1]

        #random step
        x=x+(2*random.random()-1)*stepSize
        y=y+(2*random.random()-1)*stepSize
    
        #periodic boundaries
        x=x%L
        y=y%L

        #reassign to array
        coords[i][0]=x
        coords[i][1]=y

        #output 
        print coords[i][0],",",coords[i][1]

    #mark end of timestep
    print "@"
