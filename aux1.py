# converge patterns of 2^n-1 from odd to even

n=20

for n in range(2,30):

    x=2**n-1

    print(x,bin(x))

    while x%4==3:
        x= x + (x+1)//2
        print(x,bin(x))

    print("-----")

    x= x + (x+1)//2
    print(x,bin(x))

    while x%2==0:
        x= x//2
        print(x,bin(x))

    print("------------------------")