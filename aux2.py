# odd sequence of Collatz sequence

steps=0

input_x = input("Enter a number:")

x= int(eval(input_x))

if x&1==0:
    print(x,bin(x))
    while x%2==0: x=x//2
    steps += 1

while x!=1:
    print(x,bin(x))
    x = x + (x+1)//2
    steps += 1

    while x%2==0:
        x=x//2


print(x,bin(x))
print("- {} steps. -".format(steps))
