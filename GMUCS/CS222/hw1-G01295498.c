/*
 * hw1-G01295498.c - First homework assignment of CS222 - 
 * Checking explicity of even and odd, positive or negative numbers
 *
 * Author: Craig Kimball (G01295498)
 * Date: 1/27/2022
 *
 */

#include <stdio.h>

int main()
{
	// initilization of variables
	int number;

	// assigns an inputed integer to (int) number 
	printf("Enter an integer: ");
	scanf("%d", &number);

	//Number is less than 0 and therefore negative
	if (number < 0)
	{
		//Modulus check for odd/even, ==0 checks for even
		if(number % 2 == 0)
		{
			printf("%d is negative and even.\n", number);
		}else
		{
			printf("%d is negative and odd.\n", number);
		}
		
	}
	//Number is greater than 0 and therefore positive
	else if (number > 0)
	{
		//Modulus check for odd/even, ==0 checks for even
		if(number % 2 == 0)
		{
			printf("%d is positive and even.\n", number);
		}else
		{
			printf("%d is positive and odd.\n", number);
		}
	}
	//Number is 0
	else if (number == 0)
	{
		printf("%d is zero and even\n", number);
	}

	//default return statement to conclude int method
	return 0;

}


	
