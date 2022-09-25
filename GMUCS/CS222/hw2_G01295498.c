/*
 * hw2-G01295498.c - Second homework assignment of CS222 - 
 * 
 *
 * Author: Craig Kimball (G01295498)
 * Date: 2/8/2022
 *
 */

#include <stdio.h>

int get_input();
int display(int val);

/* Main Method:
 * Calls other methods, provides logic order and returns final output
 *
 * returns int on method completion.
 */
int main()
{
    int val = get_input(); 
    int divisible = display(val);

    if(divisible == 1)
    {
        printf("%d is divisible by 9\n", val);
    
    }else{
        
        printf("%d is not divisible by 9\n",val);
    
    }



    return 0;
}

/* get_input Method:
 * Prompts the user for an integer within 1,999999
 * If the entered integer is not within these bounds it prompts the user for another
 *
 * returns int, the user defined integer
 */
int get_input()
{
    int num;

    printf("Enter an integer in range: [1, 999999]: ");
    scanf("%d",&num);

    if(num >= 1 && num <=  999999)
    {
        return num;
    }else{
        printf("Number out of range.\n");
        /*Recursive Call*/
        return get_input();
    }

    
  return num;  
}

/*display Method:
 * Parameters: 
 *      int val: Takes in a value to display each of its digits
 *
 * Method finds the sum of all digits in the integer val
 *
 * Returns int, 1 if the sum is divisible by 9, 0 otherwise
 */
int display(int val)
{
    int digit_sum = 0;

    while(val > 0)
    {

        int digit = val%10;
        val = val/10;
        digit_sum += digit;
        printf("%d\n",digit);

    }
    if(digit_sum % 9 == 0)
    {

        return 1;

    }else{

        return 0;

    }
    return 0;
}
