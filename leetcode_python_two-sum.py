# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        output = []
        numsSorted = sorted(nums)
        front = 0
        end = len(nums) - 1
        isTwoSumfound = False
        while not isTwoSumfound and front < end:
            sum1 = numsSorted[front] + numsSorted[end]
            if sum1 == target:
                if numsSorted[front] == numsSorted[end]:
                    for i,j in enumerate(nums):
                        if j == numsSorted[front]:
                            output.append(i)
                else:
                    output.append(nums.index(numsSorted[front]))
                    output.append(nums.index(numsSorted[end]))
                isTwoSumfound = True
            elif sum1 < target:
                front +=1
            elif sum1 > target:
                end -= 1

        return output



nums = [4, 3,3]

nums2 = [-1,-2,-3,-4,-5]
target2 = -8

target = 6

sol = Solution()

print (sol.twoSum(nums, target))

print(sol.twoSum(nums2, target2))





