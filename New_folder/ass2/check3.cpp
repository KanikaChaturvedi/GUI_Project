#include <bits/stdc++.h>
using namespace std;
//searchMatrix(vector<vector<int>>& matrix, int target);

 bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m=matrix.size();
        int n=matrix[0].size();
        int k=0;
        
        for(int i=0;i<m;i++)
        {
            if((matrix[i][0]<target && matrix[i][n-1]>target) || matrix[i][0]==target || matrix[i][n-1]==target)
            {
                break;
            }
            else
            {
                k++;
            }
        }

      if(k==m)
      {
        return false;
      }


        for(int i=0;i<n;i++)
        {
            if(matrix[k][i]==target)
            {
                return true;
            }
        }
        return false;
        
        
    }


int main()
{
  vector<vector<int>> matrix {
    {1}

};
int target=24;
//  searchMatrix(vector<vector<int>>& matrix, int target);
 cout<<searchMatrix(matrix,target);
 return 0;
}
 