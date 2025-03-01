# calculate the (2^m,X), the required steps from X=X(0) to X(n)<X(0)

def mod2n(x,n):  #return x%2^n
    return x&((1<<n)-1)

input_m = input("Enter a number m for 2^m:")

m= int(eval(input_m))

n = 1<<m

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

    tmp = tmp_ratio*2.0**(m-steps) if steps>m else tmp_ratio

    #print("{}, {}".format(steps,x0))

    print("({:2}, {:5}) {:5}, {:12b}".format(steps,mod2n(x0,steps), x0, x0))
 
    confirmed_ratio += tmp

    x0+=4

print("confirmed_ratio: {}".format(confirmed_ratio))