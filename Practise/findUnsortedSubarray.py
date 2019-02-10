# -*- coding: utf-8 -*-


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        nums = [2,6,4,8,10,9,15]
        arr = sorted(nums)
        
        if arr == nums:
            return 0
        
        dif = []
        
        for i in range(len(nums)):
#            if nums[i] != arr[i]:
#                dif.append(i)
            nums[i] -= arr[i]
    

        print(nums)
        a = nums.index(filter(lambda x: x!=0, nums)[0])
        b = nums.index(filter(lambda x: x!=0, nums)[-1])
        print(a,b)
        
                
#        return max(dif)-min(dif)+1