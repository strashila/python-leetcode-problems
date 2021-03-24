# https://leetcode.com/problems/jump-game/submissions/

class Solution:
    def canJump(self, nums) -> bool:
        if 0 not in nums or len(nums) == 1:
            return True
        canJump = True
        for i in range(len(nums)):            
            if nums[i] == 0 and i < len(nums) - 1: # not the last element
                canJump = False
                for j in range(i):
                    if nums[j] + j > i:
                        canJump = True
                if canJump == False:
                    return canJump

        return canJump


s = Solution()

nums1 = [2,3,1,1,4]

nums2 = [3,4,1,3,0]

nums3 = [2,0,1,0,1]

nums4 = [2,0,0]

nums5 = [0]

nums6 = [2,0,2]


nums7 = [1,0,1,0] 

print (s.canJump(nums1))

print (s.canJump(nums2))

print (s.canJump(nums3))

print (s.canJump(nums4))
print (s.canJump(nums5))
print (s.canJump(nums6))

print (s.canJump(nums7))

        
        