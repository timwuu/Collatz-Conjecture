# 2025.02.26 timijk: changed >>1 to //2
# DFS version
# print out the nested search result

import collections

A=0
B=0

nodeque= collections.deque()
node_tmp=0
node_tmp_cnt=0
confirmed_ratio=0.0
confirmed_ratio_est=0.0

input_m = eval(input("Enter a number m for 2^m:"))
N= 1<<int(input_m)

tab_n=0

def mode(tuple, A, B, level):
    global node_tmp,node_tmp_cnt
    global confirmed_ratio,confirmed_ratio_est
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
            if(A<=2048): 
                #print("{0:{width}}*{1:} {2:}".format(" ",(A,B),(a,b),width=tab_n))
                print(" / {0:}".format((a,b)),end='')
            confirmed_ratio += 4.0/A
            node_tmp_cnt+=1
        else:
            if(node_tmp<=N):
                nodeque.append(((A*2,A+B),level+1))
                nodeque.append(((A*2,B),level+1))  # small one popout first
            else:
                #print("{},{}".format((A*2,B),(A*2,A+B)))
                #print("{},{}".format(find_confirmed_ratio(B),find_confirmed_ratio(A+B)))
                if(A<=8192):
                    print("\n{0:{width}}?{1:}".format(" ",(A*2,B),width=tab_n+2),end='')
                    print("\n{0:{width}}?{1:}".format(" ",(A*2,A+B),width=tab_n+2),end='')
                confirmed_ratio_est += find_confirmed_ratio(B)+find_confirmed_ratio(A+B)
        return (a,b)

# for used in the nodeque only
def find_confirmed_ratio(x0):

    #if(x0==1): return 0.5

    steps=0

    x=x0

    while x0<=x:   # stops while x<x0
        
        if(x&1)==0:  # even
            x=x>>1
        else:
            x += (x+1)>>1
        steps += 1

    return 4.0/2.0**steps

#print("{}".format(find_confirmed_ratio(int(input_m))))

nodeque.append(((4,3),0))

max_len=len(nodeque)

while len(nodeque)>0:
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