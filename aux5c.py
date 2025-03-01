# calculate the (2^m,X), the required steps from X=X(0) to X(n)<X(0)
# including all the odd elements in the sequence

import collections

def mod2n(x,n):  #return x%2^n
    return x&((1<<n)-1)

nodeque= collections.deque()

input_N = input("Enter a number N:")

n= int(eval(input_N))

x0 = n

steps=0

x=x0

while x0<=x:   # stops while x<x0

    nodeque.append(x)

    print("seq:{}, {}, {}".format(steps,x,bin(x)))
    if(x&1)==0:  # even
        x=x>>1
    else:
        x += (x+1)>>1

    steps += 1

nodeque.append(x)

n=len(nodeque)

for i in range(n):
    x = nodeque[i]
    if( x%4==3):
        for j in range(i,n):
            if(nodeque[j]<x):
                #print("({:2}, {:5}) {:5}, {:12b}".format(j-i,x&((1<<(j-i))-1), x, x))
                print("({:2}, {:5}) {:5}, {:12b}".format(j-i,mod2n(x,j-i), x, x))
                break
    #print(i)
