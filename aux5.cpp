#include <iostream>
#include <cmath>

struct Foo
{
    int m;
    Foo()
    {
        std::cout << "Enter a number m for 2^m: "; // no flush needed
        std::cin >> m;
    }
};
 
Foo f; // static object

int mod2n( int x, int n)
{
    return x&((1<<n)-1);
}

int main()
{
    std::cout << "f.m is " << f.m << '\n';

    int n = 1<< f.m;

    int x0 = 3;  //4m+3

    double confirmed_ratio=0.0;

    double tmp_ratio = 4.0/(double)n;
    double tmp;

    int steps=0;

    int x;

    while( x0<n) {
        
        steps=0;
        x=x0;

        while( x0<=x) {
           
            if( (x&1)==0) x = x>>1;  //even
            else x+= (x+1)>>1;

            steps++;

            //std::cout<<"  -- "<< x<<"\n";

        }

        if(steps>f.m)
            tmp = tmp_ratio*pow(2.0,(double)(f.m-steps));
        else
            tmp = tmp_ratio;

        std::cout<<"( "<<steps<<", "<<mod2n(x0,steps)<<")  "<<x0<<"\n";

        confirmed_ratio += tmp;

        x0+=4;

    }

    std::cout<<"confirmed_ratio: "<< confirmed_ratio;

}