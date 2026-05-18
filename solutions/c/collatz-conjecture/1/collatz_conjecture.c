#include "collatz_conjecture.h"

int steps(int start) {
    if (start <= 0) return -1;

    unsigned int num = (unsigned int)start;
    int count = 0;

    while (num != 1) {
        if (num & 1) {
            num = num * 3 + 1;
        } else {
            num >>= 1;
        }
        count++;
    }
    return count;
}