# 2025.02.26 timijk: changed >>1 to //2
# DFS version

import collections

A=0
B=0

nodeque= collections.deque()
node_tmp=0
node_tmp_cnt=0
confirmed_ratio=0.0

input_m = input("Enter a number m for 2^m:")
N= 1<<int(eval(input_m))

def mode(tuple, level=-1):
    global A,B,node_tmp_cnt,confirmed_ratio
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
            #print("*{:15b},{}  {}".format((A+B),(A,B),(a,b)))
            confirmed_ratio += 4.0/A
            node_tmp_cnt+=1
        else:
            if(node_tmp<=N):
                nodeque.append((A*2,A+B))
                nodeque.append((A*2,B))  # small one popout first
            #print("{}{}".format((A,B),(a,b)))
        return (a,b)


nodeque.append((4,3))

max_len=len(nodeque)

while len(nodeque)>0:
    node= nodeque.pop()
    if( node_tmp!=node[0]):
        #print("{}:{}".format(node_tmp,node_tmp_cnt))
        node_tmp=node[0]
        node_tmp_cnt=0
    mode(node)

    if( len(nodeque)> max_len):
        max_len = len(nodeque) 


#print("{}:{}".format(node_tmp,node_tmp_cnt))
print("max len: {}".format(max_len))
print("confirmed_ratio={}".format(confirmed_ratio))

    # if( node[0]==8192<<8):
    #     print("{}".format(node))
    # else: 
    #     mode(node)

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