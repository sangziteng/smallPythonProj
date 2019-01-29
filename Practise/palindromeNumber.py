class Solution:
    def isPalindrome_usingStr(self, x):
        """
        https://leetcode.com/problems/palindrome-number/
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        
        s = str(x)
        if s == s[::-1]:
            return True
        return False
    
    
    def isPalindrome_notUsingStr(self, x):
        """
        https://leetcode.com/problems/palindrome-number/
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        number = x
        reverse = 0
        
        while number > 0:
            reminder = number % 10
            reverse = (reverse * 10) + reminder
            number = number // 10
        
        if reverse == x:
            return True
        return False