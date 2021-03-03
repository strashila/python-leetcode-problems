# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        output = []
        

        for i in range(0, len(nums)):
            num = nums[i]
            remainder = target - num
            for j in range(i+1, len(nums)):
                if nums[j] == remainder:
                    output.append(i)
                    output.append(j)
        return output

nums = [4, 3,3]

target = 6

sol = Solution()

print (sol.twoSum(nums, target))





