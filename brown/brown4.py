from numpy import *
import random

L=250 #system size, compatible with size of display in processing
N=20 #number of particles
r=5 #particle radius
t=0 #time
maxt=1000 #max time
stepSize=r/10. #random step size
dt=.1
gamma=1.
kbt=1.
MAXFORCE=10000000. #figure this out; it's a hack

#lennard jones params
epsilon=10000. #depth of lennard jones potential
s=2*r
s6=s**6 #particle "radius" is r
s12=s6**2

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

#run the simulation
for t in range(0,maxt):
    for i in range(0,N):
        x=coords[i][0]
        y=coords[i][1]

        #random step

        #linear
        #x=x+(2*random.random()-1)*stepSize
        #y=y+(2*random.random()-1)*stepSize

        #gaussian
        #x=x+random.gauss(mu,sigma)*stepSize
        #y=y+random.gauss(mu,sigma)*stepSize
    
        #brownian step

        # sum forces
        U=0.

        for j in range(0,N):
            if j!=i:
                dx=coords[j][0]-coords[i][0]
                dy=coords[j][1]-coords[i][1]

                dr=sqrt(dx**2+dy**2)
                dr2=dr**2

                #periodic calc (not necessary on compact surfaces)
                #if dx>(L/2)d
                #dx=dx%L
                #dy=dy%L
        
                #math calculations for LJ interaction
                dr7=dr**7
                dr13=dr**13
               
                # the LJ force in x and y
                U=-24*epsilon*(2*s12/dr13 - s6/dr7)

                if (U>MAXFORCE):
                    U=MAXFORCE

                #calculate the angle
                theta=arcsin(dy/dr)
                Ux=-U*cos(theta)
                Uy=-U*sin(theta)
        
        #add LJ force to random kick to update positions

        #position change due to random Brownian kicks
        Bdx=sqrt(2*kbt*dt/gamma)*random.gauss(mu,sigma)
        Bdy=sqrt(2*kbt*dt/gamma)*random.gauss(mu,sigma)

        #position change due to summed non-Brownian forces
        Fdx=(dt/gamma)*Ux
        Fdy=(dt/gamma)*Uy


        #print Fdx/Bdx, Fdy/Bdy

        #update the postitions
        x=x+Bdx+Fdx
        y=y+Bdy+Fdy

        #x=x+(dt/gamma)*Ux+sqrt(2*kbt*dt/gamma)*random.gauss(mu,sigma)
        #y=y+(dt/gamma)*Uy+sqrt(2*kbt*dt/gamma)*random.gauss(mu,sigma)
        
        #periodic boundaries
        x=x%L
        y=y%L

        #reassign to coordinate array
        coords[i][0]=x
        coords[i][1]=y

        #output 
        print coords[i][0],",",coords[i][1]

    #mark end of timestep
    print "@", t
