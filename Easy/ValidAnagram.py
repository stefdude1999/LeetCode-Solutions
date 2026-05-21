class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map_s = {}
        my_map_t = {}

        for i in s:
            if i not in my_map_s:
                my_map_s[i] = 1
            else:
                my_map_s[i] += 1
        
        for i in t:
            if i not in my_map_t:
                my_map_t[i] = 1
            else:
                my_map_t[i] += 1
        
        if my_map_t == my_map_s:
            return True
        else:
            return False
        
            