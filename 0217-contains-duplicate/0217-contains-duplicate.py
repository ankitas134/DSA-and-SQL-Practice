class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''nums.sort()
        
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
            return False'''
        seen=set() #setup
        for num in nums:  #one num at a time
            if num in seen: #if num exists
                return True
            seen.add(num) #add it to the seen list
        return False