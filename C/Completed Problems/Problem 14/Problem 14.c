#include <stdio.h>

long lenCollatz(long num, long *array)
{
    long temp;
    if (num == 1)
        return 1;
    else if (num < 1000000) {
        if (array[num] != 0) {
            printf("Array non-zero");
            return array[num];
        }
    }
    if (num % 2 == 0)
        temp =  1 + lenCollatz(num/2, array);
    else
        temp = 1 + lenCollatz(3*num + 1, array);
    /* if (num < 1000000) */
        /* array[num] = temp; */
    return temp;
}

int main(int argc, char **argv)
{
    long Collatz[1000001] = {0};
    long lenLongestCollatz, longestCollatz, value;
    for (long i = 1; i < 1000001; i++)
    {
        value = lenCollatz(i, Collatz);
        if (value > lenLongestCollatz)
        {
            lenLongestCollatz = value;
            longestCollatz = i;
        }
    }
    printf("Longest Collatz is %ld, which is %ld long\n", longestCollatz, lenLongestCollatz);
    return 0;
}
