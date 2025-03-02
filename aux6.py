# check the 3n+1 with the odd numbers

def mod2n(x,n):  #return x%(2^n)
    return x&((1<<n)-1)

input_N = input("Enter a number N:")

N= int(eval(input_N))

for n in range(1,N,2):
    x = 3*n+1
    #print("({0:3}, {1:5}) {0:12b}, {1:12b}".format(n,x))
    while x&1==0:
        x= (x>>1)
    print("({0:3}, {1:5}, {2:5}) {0:12b}, {1:12b}, {2:12b}".format(n,3*n+1,3*x+1))

