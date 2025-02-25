import collections

A=0
B=0

nodeque= collections.deque()

def mode(tuple, level=-1):
    global A,B
    a=tuple[0]
    b=tuple[1]

    if( level==-1):
        A=a
        B=b
        level=0

    if(a%2==0):
        if(b%2==0):
            return mode((a>>1,b>>1),level)
        else:
            return mode(((a>>1)*3,(b>>1)*3+2),level)
    else:
        if(a<A):
            print("*{}{}".format((A,B),(a,b)))
        else:
            nodeque.append((A<<1,B))
            nodeque.append((A<<1,A+B))
            print("{}{}".format((A,B),(a,b)))
        return (a,b)

        # #expand
        # a1=a<<1
        # b1=a+b
        # #test for(a1,b), (a1,b1)
        # print("  {}".format((a1,b)))
        # print("  {}".format((a1,b1)))

nodeque.append((4,3))

while len(nodeque)>0:
    node= nodeque.popleft()
    if( node[0]==8192):
        print("{}".format(node))
    else: 
        mode(node)

# mode((4,3))  #(9,8)
# mode((8,3))  #--(9,4)
# mode((16,3))   #--(9,2)*
# #mode((32,3))     #--(9,1)
# #mode((32,19))    #--(27,17)

# mode((16,11))  #--(27,20)
# mode((32,11))    #--(27,10)*

# mode((32,27))    #--(81,71)
# mode((64,27))      #--(243,107)
# mode((128,27))       #--(729,161)
# mode((128,91))       #--(243,175)

# mode((64,59))      #--(81,76)
# mode((128,59))       #--(81,38)*

# mode((128,123))      #--(243,236)

# mode((8,7))  #--(27,26)
# mode((16,7))   #--(27,13)
# mode((32,7))     #--(81,20)
# mode((64,7))       #--(81,10)
# mode((128,7))       #--(81,5)*

# mode((128,71))      #--(243,137)

# mode((64,39))      #--(243,152)
# mode((128,39))       #--(243,76)
# mode((128,103))      #--(729,593)

# mode((32,23))    #--(27,20)*

# mode((16,15))  #--(81,80)
# mode((32,15))    #--(81,40)
# mode((64,15))    #--(81,20)
# mode((128,15))       #--(81,10)*

# mode((128,79))      #--(243,152)

# mode((64,47))    #--(243,182)
# mode((128,47))       #--(243,91)
# mode((128,111))      #--(729,638)

# mode((32,31))    #--(243,242)
# mode((64,31))    #--(243,121)
# mode((128,31))       #--(729,182)
# mode((128,95))      #--(243,182)

# mode((64,63))    #--(729,728)
# mode((128,63))    #--(729,364)
# mode((128,127))    #--(2187,2186)
# mode((256,127))    #--(2187,1093)
# mode((256,255))    #--(6561,6560)


# 4n+1 -> 3n+1
# 4n+3 -> 6n+5 -> 9n+8
# 8n+3 -> 12n+5 -> 18n+8 -> 9n+4
#   16m+3 -> 18m+4 -> 9m+2
#   16m+11 -> 24m+17 -> 18m+13 -> 27m+20
# 8n+7 -> 12n+11 -> 18n+17 -> 27n+26
#   16m+7 -> 27m+13
#   16m+15 -> 54m+53 -> 81m+80


# if x<=4m, for all x, x converges to 1
#    4m+1 will converge to 1, because 4m+1, 12m+4, 3m+1
#    4m+2 will converge to 1
#    4m+3 ?
#    4m+4 will converge to 1
#    4m+5 will converge to 1, because 4m+5, 12m+16, 3m+4 if m>=3
#    4m+6 will converge to 1, 4m+6, 2m+3