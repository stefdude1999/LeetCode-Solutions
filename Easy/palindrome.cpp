#include<iostream>
#include <string>
#include <vector>
using namespace std;

void removeSpecialCharacter(string &s) 
{ 
    for (int i = 0; i < s.size(); i++) { 
        int c = s[i]; 
        if (isupper(c))  
            s[i] = tolower(c);  
        // Finding the character whose  
        // ASCII value fall under this 
        // range 
        if (s[i] < 'A' || s[i] > 'Z' && 
            s[i] < 'a' || s[i] > 'z')  
        {    
            // erase function to erase  
            // the character 
            s.erase(i, 1);  
            i--; 
        } 
    } 
    cout << s; 
} 

bool isPalindrome(string s) {
    vector<char> vec;
    removeSpecialCharacter(s);
    int size = s.size()/2;
    for (int i = 0; i < size; i++) {
        vec.push_back(s[i]);
    } 

    int lPtr = 0;
    int rPtr = s.size() - 1;
    while (lPtr != size) {
        if (s[lPtr] != s[rPtr]) {
            return false;
        }
        lPtr ++;
        rPtr --;
    }



    return true;
}

int main()
{
    string s = "A man, a plan, a canal: Panama";
    cout << isPalindrome(s) << endl;
	return 0;
}
