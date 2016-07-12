#include <stdio.h>

int lenCollatz(int num, int *array)
{
    int temp;
    if (num == 1)
        return 1;
    else if (num <= 1000000 && array[num])
    {
        return array[num];
    }
    else if (num % 2 == 0)
        temp =  1 + lenCollatz(num/2, array);
    else
        temp = 1 + lenCollatz(3*num + 1, array);
    if (num <= 1000000)
        array[num] = temp;
    return temp;
}

int main(int argc, char **argv)
{
    int Collatz[1000001];
    int lenLongestCollatz, longestCollatz, value;
    for (int i = 1; i < 1000001; i++)
    {
        value = lenCollatz(i, Collatz);
        if (value > lenLongestCollatz)
        {
            lenLongestCollatz = value;
            longestCollatz = i;
        }
    }
    printf("Longest Collatz is %d, which is %d long\n", longestCollatz, lenLongestCollatz);
    return 0;
}
