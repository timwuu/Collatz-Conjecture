# odd sequence of Collatz sequence

steps=0

input_x = input("Enter a number:")

x= int(eval(input_x))

if x&1==0:
    print("{0:5} {0:15b}".format(x))
    while x%2==0: x=x//2
    steps += 1

while x!=1:
    print("{1:}:{0:5} {0:15b}".format(x,steps))
    x = x + (x+1)//2
    steps += 1

    while x%2==0:
        x=x//2


print("{1:}:{0:5} {0:15b}".format(x,steps))
