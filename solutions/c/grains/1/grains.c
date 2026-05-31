#include "grains.h"
uint64_t square (uint8_t index) {
    if (index == 0 || index > 64) {
        return 0;
    }
    uint8_t exp = index-1;
    uint64_t result = 1ULL << exp;
    return result;
}

uint64_t total (void) {
    return UINT64_MAX;
}