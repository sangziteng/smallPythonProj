# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, string):
        """
        :type s: str
        :rtype: bool
        """
       
        string = '[](]((((({}}))))))'
        matchpairs = {'(':-1, ')':1, '[':-2, ']':2, '{':-3, '}':3}
    
        
        stack = []
        for i in string:
            if stack == []:
                stack.append(i)
                continue
            print(matchpairs[stack[-1]])
            if matchpairs[stack[-1]] + matchpairs[i] == 0:
                stack.pop()
            else:
                stack.append(i)
        
        if stack != []:
            return False
        return True
        print(stack)
    
       
        
        
        
        #2nd way       
        while '()' in string or '[]' in string or '{}' in string:
            string = string.replace('()','')
            string = string.replace('[]','')
            string = string.replace('{}','')
        print('1::::', string) 
        
        if string == '':
            return True
        return False
        