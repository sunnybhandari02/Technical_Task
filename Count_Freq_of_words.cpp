#include<bits/stdc++.h>
using namespace std;
 
#define ll		long long
#define pb 		push_back
#define endl	"\n"
#define fast	std::ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);	
#define MOD		(int) 1e6+2

class CountWords
{
public:
	string str;
	CountWords(string str2)		// Parameterized Constructor
	{
		str=str2;
	}
	void display()		// Function to display string 
	{
		cout<<str;
	}
	void FreqOfWord()		// function to count freq of each word in the string
	{
		map<string,int>mp;
		string str1="";
		for(int i=0;i<str.size();i++)
		{
			if((str[i]>=65 && str[i]<=90) || (str[i]>=97 && str[i]<=122))
			{
				str1+=str[i];
			}
			else if(str[i]>=32 && str[i]<=46)
			{	
				if(str1!="")
					mp[str1]++;
				str1="";
			}
		}
		for(auto it:mp)
		{
			cout<<it.first<<" "<<it.second<<endl;
		}
	}
};

signed main()
{
	fast;
	string str;
	getline(cin,str);
	CountWords obj(str);		// creating object of class CountWords
	// obj.display();
	obj.FreqOfWord();
	
}