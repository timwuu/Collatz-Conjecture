# 2025.02.26 timijk: changed >>1 to //2
# DFS version
# search for a particular number at a certain node such as 27 at (32,27)

import collections
import math

A=0
B=0

nodeque= collections.deque()
node_tmp=0
node_tmp_cnt=0
confirmed_ratio=0.0
confirmed_ratio_est=0.0

input_n = eval(input("Enter a number n:"))
N= int(input_n)
node_n = 2**(int( math.log2(N))+1)

tab_n=0

def mode(tuple, A, B, level):
    global node_tmp,node_tmp_cnt
    global tab_n
    a=tuple[0]
    b=tuple[1]

    if(a&1==0):
        if(b&1==0):
            return mode((a//2,b//2),A,B,level)
        else:
            return mode(((a//2)*3,(b//2)*3+2),A,B,level)
    else:
        if(a<A):
            print(" / {0:}".format((a,b)),end='')
            confirmed_ratio += 4.0/A
            node_tmp_cnt+=1
        else:
            nodeque.append(((A*2,B),level+1))
        return (a,b)

#print("{}".format(find_confirmed_ratio(int(input_m))))

nodeque.append(((node_n,N),0))

max_len=len(nodeque)



for i in range(10):

    if len(nodeque)==0: break

    node, level= nodeque.pop()

    tab_n= level<<2
    print("\n{0:{width}}{1:}".format(" ",node,width=tab_n),end='')
    #print("{0:{width}}{1:} L:{2:}".format(" ",node,level,width=tab_n))

    if( node_tmp!=node[0]):
        #print("{}:{}".format(node_tmp,node_tmp_cnt))
        node_tmp=node[0]
        node_tmp_cnt=0

    mode(node,node[0],node[1],level)

    if( len(nodeque)> max_len):
        max_len = len(nodeque) 


#print("{}:{}".format(node_tmp,node_tmp_cnt))
print()
print("max len: {}".format(max_len))
print("confirmed_ratio={:8f}".format(confirmed_ratio))
print("confirmed_ratio_est={:8f}".format(confirmed_ratio_est))

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