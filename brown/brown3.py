from numpy import *
import random
L=250 #system size, compatible with size of display in processing
N=40 #number of particles
r=5 #particle radius
t=0 #time
maxt=1000 #max time
stepSize=r/10. #random step size

#gaussian parameters
sigma=1.;
mu=0.;

#coordinates array
coords=zeros((N,2))+L/2. #start all particles in the center

#put coordinates in a line
x=3*2*r
y=3*2*r
for i in range(0,N):
    coords[i][0]=x;
    coords[i][1]=y;
    x=x+3*2*r
    if x>(L-3*2*r):
        x=3*2*r
        y=y+3*2*r

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
        #x=x+(2*random.random()-1)*stepSize
        #y=y+(2*random.random()-1)*stepSize
        x=x+random.gauss(mu,sigma)*stepSize
        y=y+random.gauss(mu,sigma)*stepSize
    
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
