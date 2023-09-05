#include<iostream>
#include<queue>
using namespace std;

void cal(string str)
{
    queue<string> q;
    q.push(str);
    while(!q.empty())
    {
        string str1= q.front();
        size_t index= str1.find('?');
        if(index != string::npos)
        {
            str1[index]='0';
            q.push(str1);

            str1[index]='1';
            q.push(str1);
        }
        else{
            cout<<str1<<endl;

        }
        q.pop();
    }
}





int main()
{
    string str="1??0?101";
    cal(str);
}