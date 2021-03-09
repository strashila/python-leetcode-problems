def searchInsert(nums, target):
    for i in range (len(nums)):
        if nums[i] == target:
           return i # target found
    
    for i in range(0, len(nums)):
        if nums[i] > target:
           return i # the target place will be at i index now
           
    return len(nums) # the target should be last

 
 
print (searchInsert([1,3,2, 2, 2, 4, 9, 22, 22], 7))