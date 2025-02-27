# using form 3:
#    n = p*2^(m+1) + q*(2^m-1), q in {0,1}
#    g(n,m)= (n+1)*3^m/2^m - 1 = (2p+1)*3^m-1
#    f(n) = p if q==0 else g(n,m)
#
# some simple cases:
#    2^m-1 becomes 3^m-1

steps=0

input_x = input("Enter a number:")

x= int(eval(input_x))

m=0
m_sum=0

#for i in range(100):
while x!=2:
    if x & 1: #odd number
        if(m==0): print("m:{},x:{}".format(m,x))
        x=x>>1
        m+=1
    else: #even number
        if m!=0:
            x= (x+1)*3**m-1   # 2025.02.27 timijk: x=2p
            print("m:{}".format(m))
            #print("m:{},x:{}".format(m,x))
            m_sum+=m
            m=0 #reset m
        else:
            x=x>>1
   
    #print(x,bin(x))

print("total of m:{}".format(m_sum))

#print(x,bin(x))
#print("- {} steps. -".format(steps))

