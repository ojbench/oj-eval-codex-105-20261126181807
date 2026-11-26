#include <iomanip>
#include <iostream>

int main() {
    int n, m;
    if (!(std::cin >> n >> m)) {
        return 0;
    }

    const int target_remaining = n - m;
    long double expectation_sum = 0.0L;
    long double expectation = 0.0L;
    for (int remaining = target_remaining + 1; remaining <= n; ++remaining) {
        // Next remaining count is uniform on [0, remaining - 1].
        // States at or below target_remaining need no further days.
        expectation = 1.0L + expectation_sum / remaining;
        expectation_sum += expectation;
    }

    std::cout << std::fixed << std::setprecision(2) << expectation << '\n';
    return 0;
}
