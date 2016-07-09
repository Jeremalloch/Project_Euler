#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPythag(int a, int b, int c)
{
    return (((a*a) + (b*b)) == (c*c)) && (a < b);
}

int main(int argc, char **argv)
{
    int a = 1 , b = 1, c = 1;
    for (b = 1; b < 500; b++)
    {
        for (a = 1; a < b; a++)
        {
            c = 1000 - (a + b);
            if (isPythag(a, b, c))
            {
                int answer = a*b*c;
                printf("The product of a x b x c is: %d\n", answer);
                printf("a = %d   b = %d   c = %d\n", a, b, c);
            }
        }
    }
    
	return 0;
}
