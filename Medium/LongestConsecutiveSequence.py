class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            #check if it's the start of a sequence
            if (n - 1) not in numSet: #if no left neighbour, start of a sequence
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest