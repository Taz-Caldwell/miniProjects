#include <stdio.h>

int main(void) {
    int x, y, z;

    for (int i = 0; i < 2; i++) {
        x = 0;
        y = 1;
        do {
           printf("%d\n", x);

           z = x + y;
           x = y;
           y = z; 
        } while (x < 100000);
    }
}
