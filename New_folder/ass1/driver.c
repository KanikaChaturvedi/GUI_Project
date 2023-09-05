#include <stdio.h>
#include "myheader.h"

int main( int argc, char const *argv[])
{
    int a=10, b=20;
    int r= add(a,b);
    printf("result: %d\n", r);
    return 0;
}