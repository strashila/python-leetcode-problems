# https://leetcode.com/problems/sort-colors/submissions/

class Solution:
    def sortColors(self, nums) -> None:
        
        isSorted = False
        
        while not isSorted:
            isSorted = True
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    isSorted = False
                    c = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = c

        

s = Solution()

nums = [2,0,2,1,1,0]

s.sortColors(nums)
print (nums)