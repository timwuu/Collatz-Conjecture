# calculate the (2^m,X), the required steps from X=X(0) to X(n)<X(0)

input_N = input("Enter a number:")

N= int(eval(input_N))

n = 1<<N

x0 = 3  #4m+3

confirmed_ratio=0.0

tmp_ratio = 4.0/n

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

    tmp = tmp_ratio*2.0**(N-steps) if steps>N else tmp_ratio

    print("{}, {}".format(steps,x0))

    confirmed_ratio += tmp

    x0+=4

print("confirmed_ratio: {}".format(confirmed_ratio))