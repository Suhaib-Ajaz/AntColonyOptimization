import itertools
import math
import random
import numpy as np
from itertools import repeat

def check(lst):
    repeat=list(itertools.repeat(lst[0],len(lst)))
    return repeat==lst
def minim(lis,n):
    minpos=lis.index(min(lis))
    return minpos

def update(t1,t2,best1,best2,ratio):
    print("pheromone values:")
    print(t1)
    print(t2)

    t1old=t1[best1]
    t2old=t2[best2]
    for i in range(0, len(t1)):
        t1[i]=(1-ro)*t1[i]
    for i in range(0, len(t2)):
        t2[i]=(1-ro)*t2[i]
    t1[best1]=t1old+(q*ratio)
    t2[best2]=t2old+(q*ratio)



def prob(t1,t2):
    p1=[]
    p2=[]

    for i in range(0,len(t1)):
        p1.append(t1[i]/(sum(t1)))

    for i in range(0, len(t2)):
        p2.append(t2[i] / (sum(t2)))
    print("Cumulative probablities:" )
    rang1=[]
    a=0
    for i in range(0,len(p1)):
        rang1.append([a,p1[i]+a])
        a=a+p1[i]

    print(rang1)
    rang2 = []
    a = 0
    for i in range(0, len(p2)):
        rang2.append([a, p2[i] + a])
        a = a + p2[i]
    print(rang2)
    r1=np.random.random_sample(5)
    r2=np.random.random_sample(5)
    print("Random numbers for roulette wheel selection:")
    print(r1)
    print(r2)
    antx=[]
    anty=[]

    for j in range(0,len(r1)):

        for i in range(0,len(rang1)):
            if r1[j] >rang1[i][0] and r1[j] <= rang1[i][1] :
                antx.append(var1[i])

    for j in range(0,len(r2)):

        for i in range(0,len(rang2)):
            if r2[j] >rang2[i][0] and r2[j] <= rang2[i][1] :
                anty.append(var2[i])


    print("Variable selection by ants in direction x1: ")
    print(antx)
    print("Variable selection by ants in direction x2: ")
    print(anty)
    farr=[]
    for i in range(0,len(antx)):
        farr.append(math.pow(antx[i],2) + math.pow(anty[i],2))
    print("Objective functions of each ant:")
    print(farr)
    minn=minim(farr,len(farr))
    fbest=min(farr)
    fworst=max(farr)
    fratio=fbest/fworst
    print("Best objective function "+str(fbest)+"***** Worst objective function "+str(fworst))
    bestant=minn
    bx=antx[bestant]
    by=anty[bestant]
    bant1=var1.index(bx)
    bant2=var2.index(by)
    print("Best path/variables in iteration: x1 "+str(bx)+" x2 "+str(by))
    update(t1,t2,bant1,bant2,fratio)
    return antx,anty,bx,by



n=5   #ant no
iter=100
ro=0.5
q=2
x1=0
x2=0
var1=[3,2,.2,4.5,-4,]
var2=[1.2,3,-3.5,4.2]
f= math.pow(x1,2) + math.pow(x2,2)
t1=[1,1,1,1,1]
t2=[1,1,1,1]
for i in range(0,100):
        print("iteration ",i)
        antx,anty,bx,by=prob(t1, t2)
        ch1=check(antx)
        ch2=check(anty)
        print("**************************************************************\n\n")
        if ch1==True and ch2==True:
            break

print("Objective obtained--------------------")
print("The best path/variables :")
print("x1--> "+str(bx)+"    x2--> "+str(by))







