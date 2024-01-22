#include "iostream"
 
using namespace std;
long int a, first_num, ans;
int main() {
    cin >> a;
    for (long int i = 0; i < a; i++) {
        if (i == 0) {
            cin >> first_num;
        }
        else {
            long int k;
            cin >> k;
            if (k == first_num) {
                ans += 1;
            }
        }
    }
    cout << ans;
}


