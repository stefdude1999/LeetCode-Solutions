class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #this is good if time is contsraint. Use n^2 solution if space is the issue
        my_map = {}
        for i in range(len(nums)):
            my_map[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in my_map.keys() and my_map.get(target - nums[i]) != i:
                sol = list()
                sol.append(i)
                sol.append(my_map.get(target - nums[i]))
                return sol
        
        return list()
                 
        