# -*- coding: utf-8 -*-

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = "IIIIVIV"
        num = 0
        
        dic = {'I':1, 
              'V':5,
              'X':10,
              'L':50,
              'C':100,
              'D':500,
              'M':1000}
        
        dic_sub = {'IV':4,
                  'IX':9,
                  'XL':40,
                  'XC':90,
                  'CD':400,
                  'CM':900}
        
        for ds in dic_sub.keys():
            for i in range(len(s)):
                if ds in s:
                    num += dic_sub[ds]
                    s = s.replace(ds,'',1)
                    #s.remove(ds)
            
        for d in dic:
            for i in range(len(s)):
                if d in s:
                    num += dic[d]
                    s = s.replace(d,'',1)
                
        print(s)
        print(num)
        

                
                