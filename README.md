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
aux5.py  
&nbsp;&nbsp;&nbsp; Calculate the required steps for all the x%4=3 cases < 2^m from n to n<sub>i</sub>, n<sub>i</sub><n.  
&nbsp;&nbsp;&nbsp; It's the bounded stop time of n, where n ≡ 3 (mod 4).  
aux7.py  
&nbsp;&nbsp;&nbsp; Check the 3^n-1 binary form for 2^n-1.  

## Comments:  
If n ≡ 3 (mod 4), can converge, it means we can find an integer m and 2^m+n can also converge, vice versa.
n and 2^m+n has the same stop time, so do all the integers have the form of a*2^m+n.
It means the stop time of any integer in the form of a*2^m+n is bounded.
If we have can find the m for n, does it imply all the positive integers n ≡ 3 (mod 4) have a bounded stop time?  
Using aux5.py to calculate the pair (m,n), n ≡ 3 (mod 4), m is the bounded stop time of n.  
Using aux8.py to calculate the pair (m,n) for a specific n using inference.  
Using aux2.py to show all the odd sequency.
