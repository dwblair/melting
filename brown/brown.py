import random
L=250 #compatible with size of display in processing
N=10
r=10
t=0
maxt=10
print "#N L r"
print N,",",L,",",r
print "#coords"
for t in range(0,maxt):
    for i in range(0,N):
        x=random.random()*L;
        y=random.random()*L;
        print x,",",y
    print "@"
