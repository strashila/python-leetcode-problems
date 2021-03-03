# https://leetcode.com/problems/valid-parentheses/

class Solution:
    
    def isValid(self, s):

        parentheses_list = ['{}', '[]', '()']        

        are_parents_left = True

        while are_parents_left:
            
            are_parents_left = False

            for parent in parentheses_list:
                if parent in s:
                    are_parents_left = True
                    s = s.replace(parent, '')
        if len(s) > 0:
            return False
        else:
            return True
       
s = Solution()

teststr = "{[()]}{}{}{}{}"
print(s.isValid(teststr))


