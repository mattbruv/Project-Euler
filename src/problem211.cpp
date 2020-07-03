#include <iostream>
#include <math.h>

long long sumDivSquares(long long number) {
    long long total = 0;
    int limit = (int) sqrt(number);
    for (long long i = 1; i <= limit; i++) {
        if (number % i == 0) {
            total += i * i;
            long long n = number / i;
            if (i != n) {
                total += n * n;
            }
        }
    }
    return total;
}

bool isPerfectSquare(long long number) {
    if (sqrt(number) == floor(sqrt(number))) {
        return true;
    }
    return false;
}

int main() {
    long long total = 0;
    for (long long i = 1; i < 64000000; i++) {
        if (isPerfectSquare(sumDivSquares(i))) {
            total += i;
        }
    }
    std::cout << total << std::endl;
    // 1922364685
    // real    63m3.445s
    return 0;
}
