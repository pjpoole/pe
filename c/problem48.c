#include <stdio.h>

#define mod 10000


int main(){

	// some counter variables
	int n, k;

	// p = power, somehow
	// s = sum?
	// t = temp?
	unsigned int p2, p1, p0;
	unsigned int s2, s1, s0;
	unsigned int t2, t1, t0;
	
	// s = 0 -> clearly
	s2 = s1 = s0 = 0;
	
	for( n=1 ; n<=1000 ; n++ ){   // do this 1000 times == for all integers less than 1000
	   // p = 1
	   p2 = p1 = 0; p0 = 1;
	   for( k=1 ; k<=n ; k<<=1 ); // next power of two greater than n?
	   while( k>>=1 ){			  // rightshift without loop until 0,
		   // p *= p				 generate last 12 digits of the power (how?)
		   t0 = p0*p0;
		   t1 = 2*p0*p1 + t0/mod;
		   t2 = 2*p0*p2 + p1*p1 + t1/mod;
		   p0 = t0%mod;
		   p1 = t1%mod;
		   p2 = t2%mod;
		   if( n&k ){			// n and k have a bit in common
			   // p *= n
			   t0 = p0*n;
			   t1 = p1*n + t0/mod;
			   t2 = p2*n + t1/mod;
			   p0 = t0%mod;
			   p1 = t1%mod;
			   p2 = t2%mod;
			   }
	   }
	   // s += p
	   t0 = p0+s0;
	   t1 = p1+s1 + t0/mod;		// carries from t0's excess
	   t2 = p2+s2 + t1/mod;		// same
	   s0 = t0%mod; 			// we're only keeping 12 digits
	   s1 = t1%mod;
	   s2 = t2%mod;
	
	}
	printf("ex48: %02d%04d%04d\n", s2%100, s1, s0); // print 10 digits
	
	return 0;
} 