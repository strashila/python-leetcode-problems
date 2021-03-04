class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        
        for i in range (len(haystack)):
            substr = haystack[i:i+len(needle)]            
            if substr == needle:
                return i
        return -1

s = Solution()
print (s.strStr("hello", "ll"))