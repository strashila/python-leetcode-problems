import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        match = str.lower(re.sub(r'[^\w]+', '', s))
        newstr = ''
        for i in range(1, len(match)+1):
            newstr = newstr + match[-i]
        if match == newstr: return True

        return False


sol = Solution()
strstre = "A man, a plan, a canal: Panama"

match = re.sub(r'[^\w+]', '', strstre)

s = ''
for i in range(1, len(match)+1):
    s = s + match[-i]

print(match)

print (s)

print (sol.isPalindrome(strstre))
        
        