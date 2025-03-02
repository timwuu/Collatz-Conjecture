# form 3: n = p*2^(m+1) + q*(2^m-1), q in {0,1}  
#     g(n,m)= (n+1)*3^m/2^m - 1 = (2p+1)*3^m-1  
# for p=0, g(n,m) = 3^m-1

# calculate g(n,m) for p=0, m=1 to N

def mod2n(x,n):  #return x%(2^n)
    return x&((1<<n)-1)

input_N = input("Enter a number N:")

N= int(eval(input_N))

for n in range(1,N+1):
    x = 3**n-1

    #while x&1==0:
    #    x=x>>1
    print("({0:7}, {1:10}) {1:40b}".format(2**n-1,x))

