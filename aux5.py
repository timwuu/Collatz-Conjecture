# calculate the (2^m,X), the required steps from X=X(0) to X(n)<X(0)

input_N = input("Enter a number:")

N= int(eval(input_N))

n = 1<<N

x0 = 3  #4m+3

while x0 < n:

    steps=0

    x=x0

    while x0<=x:   # stops while x<x0
        #print(x,bin(x))
        if(x&1)==0:  # even
            x=x>>1
        else:
            x += (x+1)>>1
    
        steps += 1
           
    print("{}, {}".format(steps,x0))

    x0+=4
