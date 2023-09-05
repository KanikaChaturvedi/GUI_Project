#include <bits/stdc++.h>
using namespace std;
// Driver code
int main()
{
    std::vector<int> v{10, 20, 30, 40, 50};

    // Print vector
    std::cout << "Vector contains :";
    for (int i = 0; i < v.size(); i++)
        std::cout << " " << v[i];
    std::cout << "\n";

    std::vector<int>::iterator upper1, upper2;

    // std :: upper_bound
    upper1 = std::upper_bound(v.begin(), v.end(), 9);
    upper2 = std::upper_bound(v.begin(), v.end(), 90);

    std::cout << "\nupper_bound for element 35 is at position : "
              << (upper1 - v.begin());
    std::cout << "\nupper_bound for element 45 is at position : "
              << (upper2 - v.begin());

    // return 0;
    // bool neg=1;
    // if(neg){
    //     cout<<neg;
    // }
    return 0;
}
