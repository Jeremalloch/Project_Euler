#include <stdio.h>

long long choose(long long n, long long k)
{
    long long r = 1;
    for (long long divisor = 1; divisor <= k; k++)
    {
        r *= n--;
        r /= divisor;
    }
    return r;
}

int main(int argc, char **argv)
{
    // The number of possible routes only going down or right in a sqaure nxn 
    // grid is equal to 2nCn, or (2n!)/(n!*(2n-n)!)
    printf("A 20x20 grid has %llu possible routes from top left to bottom right\n", choose(20,20));
}
