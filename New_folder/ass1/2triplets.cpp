#include<bits/stdc++.h>
using namespace std;

void cal(int arr[], int n)
{
    
    bool found =false;

    for (int i=0;i<n-1;i++)
    {
         unordered_set<int> s;
        for (int j=i+1;j<n;j++)
        {
            int x= -(arr[i] + arr[j]);
            if(s.find(x) != s.end())
            {
                found = true;
                printf("%d, %d, %d\n",x,arr[i],arr[j]);
            }
            else
               s.insert(arr[j]);        
        }   
    }
if(found==true)
    {
    cout<<"there exists triplets\n";
    }
else
    cout<<"nope";

}
 int main()
{
    int arr[] = {0, -1, 2, -3, 1};
    int n = sizeof(arr)/sizeof(arr[0]);
    cal(arr, n);
    return 0;
}