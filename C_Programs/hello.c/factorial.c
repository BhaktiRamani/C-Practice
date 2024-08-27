#include<stdio.h>
int main()
{
    int n,fact;
    printf("enter a number for factorial : ");
    scanf("%d", &n);
    for(int i =1; i<=n;i++)
    {
        fact = fact*i;
    }
    printf("factorial of n is : %d ", fact);
}