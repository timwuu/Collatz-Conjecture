# 2025.02.26 timijk: changed >>1 to //2

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
            return mode((a//2,b//2),level)
        else:
            return mode(((a//2)*3,(b//2)*3+2),level)
    else:
        if(a<A):
            print("*{}{}".format((A,B),(a,b)))
        else:
            nodeque.append((A*2,B))
            nodeque.append((A*2,A+B))
            print("{}{}".format((A,B),(a,b)))
        return (a,b)

nodeque.append((4,3))

while len(nodeque)>0:
    node= nodeque.popleft()
    if( node[0]==8192<<8):
        print("{}".format(node))
    else: 
        mode(node)

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