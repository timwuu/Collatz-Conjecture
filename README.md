# Collatz-Conjecture
Collatz Conjecture  

form 1  
   f(n) = n/2 if n is even else 3n+1  

form 2  
   f(n) = n/2 if n is even else (3n+1)/2  

form 3  
   n = p*2^(m+1) + q*(2^m-1), q in {0,1}  
   g(n,m)= (n+1)*3^m/2^m - 1 = (2p+1)*3^m-1  
   f(n) = p if q==0 else g(n,m)  

   g(n,1)= (3n+1)/2  
   g(n,2)= (9n+5)/4  
   g(n,3)= (27n+19)/8  

it's all about the number (2p+1)*3^m-1 ?

CollatzConjecture.py  
    Calculate all the x%4=3 cases < 2^m using BFS.  
CollatzConjecture.py  
    Calculate all the x%4=3 cases < 2^m using DFS.  
aux2.py  
    Compute the sequence and show odd numbers only.  
aux4.py  
    Use form 3 to compute the sequence.  
aux7.py  
    Check the 3^n-1 binary form for 2^n-1.  
