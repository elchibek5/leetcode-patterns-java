#include <bits/stdc++.h>
using namespace std;

int solve() {
    int a, b, c;
    cin >> a >> b >> c;

    int tryA, tryB, tryC, tryD, tryE;

    tryA = a + b + c;
    tryB = (a + b) * c;
    tryE = a * (b + c);
    tryC = a * b + c;
    tryD = a * b * c;

    return max({tryA, tryB, tryC, tryD, tryE});
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cout << solve();
}
