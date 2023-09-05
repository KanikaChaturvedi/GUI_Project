 #include<vector>
 #include<iostream>
 #include<algorithm>
 using namespace std;

#include <unordered_map>
int main()
{
  // string str="amrit";
  // for(char &ch: str)
  // {
  //   cout<<++ch<<endl;
  // }
  // char c='d';
  // cout<<str<<endl;
  // cout<<c;
  // return 0;



// unordered_map<int,int> mp;
// mp.insert({10,200});
// cout<<mp[10]<<endl;
// cout<<mp.size()<<endl;
// cout<<mp[20]<<endl;
// cout<<mp.size()<<endl;
int n=5;

 vector<int> arr({2,3,2,3,5});
        // code here
        for(int i=1;i<=n;i++)
        {
            arr[i-1]=count(arr.begin(),arr.end(),i);
            //arr[i-1]=total;
        }
        
    for(int i:arr)
    {
      cout<<i<<endl;
    }




return 0;


}














//  struct Point{
//    int x;
//    int y;
//    Point(int i, int j){
//      x=i;
//      y=j;
//    }
//  };
//  bool mycmp(Point &p1, Point &p2)
//  {
//    return p1.x < p2.x;
//  }
//  int main()
//  {
//    vector<Point> vec={{5,4},{2,300},{90,10}};
   
//    for(const Point &curr: vec)
//    {
//      cout<<curr.x<<" "<<curr.y;
//      cout<<endl;
//    }
//    auto it= max_element(vec.begin(),vec.end(),mycmp);
//    cout<<((*it).x)<<" "<<((*it).y)<<endl;
//    it= min_element(vec.begin(),vec.end(),mycmp);
//    cout<<((*it).x)<<" "<<((*it).y)<<endl;
//    return 0;
//  }
 