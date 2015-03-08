#include <stdio.h>
#include <stdlib.h>
 
int main(int argc, char **argv)
{
    unsigned long long sum=0;
    unsigned long long counter=1;
    while(1)
    {
        sum+=counter;
        counter++;
 
        int num=0;
        unsigned long long i=1;
        while(i*i<=sum)
        {
            if(sum%i==0)
            {
                num+=2;
            }
            i++;
        }
        if(num>=500)
        {
            break;
        }
    }
    printf("%llu\n",sum);
}