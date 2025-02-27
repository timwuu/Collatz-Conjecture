# calculate the (2^m,X), where converge steps when X(n)<X

input_N = input("Enter a number:")

N= int(eval(input_N))

n = 1<<N

x0 = 3  #4m+3

while x0 < n:

    steps=0

    x=x0

    if x&1==0:  #if it's even
        print(x,bin(x))
        while x%2==0: x=x//2
        steps += 1

    while x!=1:
        #print(x,bin(x))
        x = x + (x+1)//2
        steps += 1

        if x<x0:
            break

        while x%2==0:
            x=x//2

    print("{}, {}".format((steps+1),x0))

    x0+=4
