#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool isPalindrome(int number)
{
	int num, reversedNumber = 0, remainder;
	num = number;

	while (num != 0)
	{
		remainder = num % 10;
		reversedNumber = reversedNumber * 10 + remainder;
		num /= 10;
	}

	return (number == reversedNumber);
}

int main(int argc, char **argv)
{
	int largPalin = 0, temp;
	for (int i = 999; i > 99; i--)
	{
		if (i*999 < largPalin)
			break;
		for (int j = 999; j > 99; j--)
		{
			temp = i*j;
			if (temp > largPalin)
				if (isPalindrome(temp))
					largPalin = temp;
		}
	}
	printf("Largest palindrome produced by multiplying two \n"
		"three digits numbers together is: %d\n", largPalin);
	return 0;
}
