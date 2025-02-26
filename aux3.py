# odd sequence of Collatz sequence

for n in range(30,64):

    steps=0

    x = 2**n-1

    while x!=1:
        #print(x,bin(x))
        x = x + (x+1)//2
        steps += 1

        while x%2==0:
            x=x//2

    #print(x,bin(x))
    print("number 2^{}-1 requires {} steps.".format(n,steps))
