# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        strs = ['booo','bosiness','bosy']
            
        for i, letter_group in enumerate(zip(*strs)):
            #print(set(enumerate(zip(*strs))))
            print('i:', i, 'letter_group:', letter_group)
            if len(set(letter_group)) > 1:
                print(strs[0][:i])
                print(min(strs))
           
            
    def longestCommonPrefix2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        prefix = ""
        minstr = min(strs, key=len)
        lenth = len(minstr)
        
        strs.remove(minstr)
                
        for i in range(lenth):
            prefix = minstr[0:i+1]
            
            for string in strs:
                if not string.startswith(prefix):
                    prefix = prefix[:-1]
                    return prefix
                
        return prefix