#include <iostream>
#include <cmath>

bool isPrime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;

    if (n % 2 == 0 || n % 3 == 0) return false;

    for (int i = 5; i <= std::sqrt(n); i += 6) {
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    }

    return true;
}

int main() {
    int num;
    std::cout << "Enter a number to check if it's prime: ";
    std::cin >> num;

    if (isPrime(num))
        std::cout << num << " is prime!" << std::endl;
    else
        std::cout << num << " is not prime." << std::endl;

    return 0;
}
