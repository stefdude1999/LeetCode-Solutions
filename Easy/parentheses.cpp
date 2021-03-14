#include<iostream>
#include <string>
#include <vector>
using namespace std;

bool isValid(string s) {
        if ( s.size() % 2 != 0) {
            return false;   
        }
        bool result = true;
        vector<char> left;
        int rSize = 0;
        int lSize = 0;
        for(char& c : s) {
            if (c == '[' || c == '(' || c == '{') {
                cout << "left 1" << c << endl;
                left.push_back(c);
                lSize++;
            } else {
                rSize++;
                if (left.empty()) {
                    return false;
                }
                char test = left.back();
                left.pop_back();
                
                
                if (test == '(' && c != ')' || test != '{' && c != '}' || test != '[' && c != ']') {
                    return false;
                }
            }
        }  
        if (lSize != rSize) {
            return false;
        }
        
        return true;
    
    }

int main()
{
    string paran = "({{{{}}}))";
    cout << isValid(paran) << endl;
	return 0;
}
