#include <bits/stdc++.h>
using namespace std;
int main()
{
vector<int> ans(10);
//ans.push_back(8);
ans[5] = 7;
vector<int>::iterator it;
it =find(ans.begin(),ans.end(),7);
cout<<it-ans.begin();
// for(int i=0;i<10;i++)
// {
//     cout<<ans[i]<<endl;
// }
}