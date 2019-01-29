


class Solution:
    def reverse(self, x):
        """
        https://leetcode.com/problems/reverse-integer/
        :type x: int
        :rtype: int
        """    
        
        maxint = 2**31-1
        minint = -(2**31)
       
        if x > maxint or x < minint:
            return 0
        
        s = str(abs(x))[::-1]
        if int(s) > maxint or -int(s) < minint:
            return 0
    
        if x < 0:
            return -int(s)
        else:
            return int(s)