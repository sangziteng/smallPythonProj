# -*- coding: utf-8 -*-

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums = [-1,0,1,2,-1,-4]
        nums.sort()
        
        returnlist = []
        
        #if len(nums) < 3:
        #    return
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i >= j:
                    continue
                num = -(nums[i]+nums[j])
                #print(num, nums[i], nums[j])
                if num in nums:
                    newpattern = [nums[i], nums[j], nums[nums.index(num)]]
                    newpattern.sort()
                    if newpattern in returnlist:
                        continue
                    returnlist.append(newpattern)
        
        return returnlist