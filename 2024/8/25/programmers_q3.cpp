#include <iostream>
using namespace std;

int solution(int n)
{
    int ans = 0;

    while (n > 0){
        if (n % 2 == 1){
            ans += 1;
        }
        n /= 2;
    }

    // 5 -> 2 -> 1
    // 6 -> 3 -> 1
    // 5000 -> 2500 -> 1250 -> 725 ->
                            // 1

    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cout << "Hello Cpp" << endl;

    return ans;
}