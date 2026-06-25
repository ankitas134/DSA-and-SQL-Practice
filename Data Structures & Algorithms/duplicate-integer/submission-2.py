'''class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        for n in nums:
            if n in a:
                return True
            a.add(n)
        return False
         '''
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
