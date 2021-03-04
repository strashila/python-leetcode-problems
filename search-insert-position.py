def searchInsert(nums, target):
    for i in range (len(nums)):
        if nums[i] == target:
            return i # target found
    is_bigger_number = False
    for i in range(0, len(nums)):
        if nums[i] > target:
            is_bigger_number = True                
            return i # the target place will be at i index now
        
    if not is_bigger_number:
        return len(nums) # the target should be last

 
 
print (searchInsert([1,3, 4], 7))