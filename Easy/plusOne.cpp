class Solution {
public:
    void selfCall(vector<int>& digits, int x) {
        
        if (x > 0) {
            digits[x]=0;
            if (digits[x-1] != 9) {
                digits[x-1]+=1;
            } else {
                selfCall(digits, x-1);
            }
        } else {
            digits[x]=0;
            digits.insert(digits.begin(), 1);
        }
    }
    
    vector<int> plusOne(vector<int>& digits) {
        // if num @ end of list != 9, increment by 1
        if (digits[digits.size()-1] != 9) {
            digits[digits.size()-1] += 1;
        } else {
            //if (digits.size() != 1) {
                selfCall(digits, digits.size()-1);
            //}
        }
        return digits;
    }
};
