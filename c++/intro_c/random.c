#include <stdlib.h>
#include <math.h>
#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

double drand()
{
    return (rand()+1.0)/(RAND_MAX+1.0);
}

double random_normal()
{
    return sqrt(-2*log(drand())) * cos(2*M_PI*drand());
}