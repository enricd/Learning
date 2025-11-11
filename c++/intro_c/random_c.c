#include <stdio.h>
#include "random.h"

#define NUM_RND 10

int main() {
    int i;
    double rands[NUM_RND];
    for (i=0; i<NUM_RND; i++) {
        rands[i] = 1.0 + 0.5*random_normal();
        printf("%f\n", rands[i]);
    }
}