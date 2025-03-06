# 2025.02.26 timijk: changed >>1 to //2
# DFS version
# Derive the bounded stop time of a certain number.

import collections
import math

nodeque= collections.deque()

input_n = eval(input("Enter a number n:"))
N= int(input_n)
node_n = 2**(int( math.log2(N))+1)


def mode(tuple, A, B, level):
    a=tuple[0]
    b=tuple[1]

    if(a&1==0):
        if(b&1==0):
            return mode((a//2,b//2),A,B,level)
        else:
            return mode(((a//2)*3,(b//2)*3+2),A,B,level)
    else:
        if(a<A):
            print("L:{} / {} / {}".format(level,(A,B),tuple))
        else:
            nodeque.append(((A*2,B),level+1))
        return (a,b)

nodeque.append(((node_n,N),0))

for i in range(100):

    if len(nodeque)==0: break

    node, level= nodeque.pop()

    mode(node,node[0],node[1],level)
