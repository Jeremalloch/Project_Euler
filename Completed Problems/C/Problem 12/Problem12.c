#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <math.h>

long triNumber(long n)
{
    return (n+1)*n/2;
}

int numFactors(long number)
{
    long stopping = floor(sqrt(number));
    int numFactors = 0;
    for(long i = 1; i <= stopping; i++)
    {
	if (number % i == 0)
	    numFactors += 2;
    }
    return numFactors;
}


int main(int argc, char **argv)
{
    long num = 1;

    while (numFactors(triNumber(num)) < 500)
        num++;

    printf("First number is %ld\n", triNumber(num));
    printf("Number of factors of %ld is %d\n", triNumber(num), numFactors(triNumber(num)));

    return 0;
}
