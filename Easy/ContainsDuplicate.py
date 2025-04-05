class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        this_set = set()
        for i in nums:
            if i in this_set:
                return True
            else:
                this_set.add(i)
        
        return False