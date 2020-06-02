#include <iostream>
#include <math.h>

int numDivisors(int number) {
    int total = 0;
    int limit = (int) sqrt(number);
    for (int i = 1; i <= limit; i++) {
        if (number % i == 0) {
            total++;
            if (i != (int)(number / i)) {
                total++;
            }
        }
    }
    return total;
}

int main() {
    int curr = numDivisors(2);
    int next = numDivisors(3);
    int total = 0;
    for (int i = 2; i < 10000000; i++) {
        next = numDivisors(i + 1); // get divisors of next number
        // Do they have the same number of divisors?
        if (curr == next) {
            total++;
        }
        curr = next;
    }
    std::cout << total << std::endl;
    // 986262
    // real    1m29.997s
    return 0;
}
