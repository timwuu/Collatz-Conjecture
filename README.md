# Collatz-Conjecture
Collatz Conjecture  

form 1  
&nbsp;&nbsp;&nbsp; f(n) = n/2 if n is even else 3n+1  

form 2  
&nbsp;&nbsp;&nbsp; f(n) = n/2 if n is even else (3n+1)/2  

form 3  
&nbsp;&nbsp;&nbsp; n = p*2^(m+1) + q*(2^m-1), q in {0,1}  
&nbsp;&nbsp;&nbsp; g(n,m)= (n+1)*3^m/2^m - 1 = (2p+1)*3^m-1  
&nbsp;&nbsp;&nbsp; f(n) = p if q==0 else g(n,m)  

&nbsp;&nbsp;&nbsp; g(n,1)= (3n+1)/2  
&nbsp;&nbsp;&nbsp; g(n,2)= (9n+5)/4  
&nbsp;&nbsp;&nbsp; g(n,3)= (27n+19)/8  

CollatzConjecture.py  
&nbsp;&nbsp;&nbsp; Calculate all the x%4=3 cases < 2^m using BFS.  
CollatzConjectureB.py  
&nbsp;&nbsp;&nbsp; Calculate all the x%4=3 cases < 2^m using DFS.  
CollatzConjectureC.py  
&nbsp;&nbsp;&nbsp; Calculate all the x%4=3 cases < 2^m using DFS.  
&nbsp;&nbsp;&nbsp; Print out the nested search result.  
aux2.py  
&nbsp;&nbsp;&nbsp; Compute the sequence and show odd numbers only.  
aux4.py  
&nbsp;&nbsp;&nbsp; Use form 3 to compute the sequence.  
aux7.py  
&nbsp;&nbsp;&nbsp; Check the 3^n-1 binary form for 2^n-1.  

## Comments:  
If n can converge, it means we can find an integer m and 2^m+n can also converge, vice versa.
It seems there are unlimited choices of m that can satisfy the convergence of 2^m+n, such that any n can converge to 1?
