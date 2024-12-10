class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[List[int]]:
        left, right = 0, len(numbers) - 1
        results = []

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            else:
                results.append([numbers[left], numbers[right]])
                left += 1
                right -= 1

                while left < right and numbers[left] == numbers[left - 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right + 1]:
                    right -= 1

        return results

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutionsSet = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            subarray = nums[i + 1:]

            twoSumResults = self.twoSum(subarray, target)
            for res in twoSumResults:
                solutionsSet.append([nums[i], res[0], res[1]])
        
        return solutionsSet
