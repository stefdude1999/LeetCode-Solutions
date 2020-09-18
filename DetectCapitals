#include <cctype>

class Solution {
public:
    bool multipleCapitals(string word) {
        for (int i = 0; i < word.length(); i++) {
            if (!isupper(word.at(i))) {
                return false;
            }
        }
        return true;
    }
    
    bool detectCapitalUse(string word) {
       if (word.length() == 1) {
           return true;
       }
        
        
        if (word.length() == 2) {
            if (isupper(word.at(0)) && !isupper(word.at(1)) || isupper(word.at(0)) && isupper(word.at(1))) {
                return true;
            } else if (!isupper(word.at(0)) && !isupper(word.at(1))) {
                return true;
            }
            return false;
        }
        
        if (word.length() > 2) {
            if (isupper(word.at(0)) && isupper(word.at(1))) {
                return multipleCapitals(word);
            } else if (isupper(word.at(0))) {
                for (int i = 1; i < word.length(); i++) {
                    if (isupper(word.at(i))) {
                        return false;
                    }
                }
                return true;
            } else if (!isupper(word.at(0))) {
                for (int i = 1; i < word.length(); i++) {
                    if (isupper(word.at(i))) {
                        return false;
                    }
                }
                return true;
            }
        } 
        
        return true;
    }
};
