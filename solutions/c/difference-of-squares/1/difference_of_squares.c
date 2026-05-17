#include "difference_of_squares.h"
unsigned int sum_of_squares(unsigned int number) {
    //unsigned int sum = 0;
    //unsigned int x = 0;

    //while (x <= number) {
    //    sum += x*x;
    //    x++;
    //}

    //return sum;

    return (number*(number+1)*(2*number+1))/6;
}

unsigned int square_of_sum(unsigned int number) {
    //unsigned int sum = 0;

    //unsigned int x;
    //for (x = 0; x <= number; x++) {
    //    sum += x;
    //}

    //return sum*sum;

    unsigned int sum = (number*(number+1))/2;

    return sum*sum;
}

unsigned int difference_of_squares(unsigned int number) {
    return square_of_sum(number)-sum_of_squares(number);
}