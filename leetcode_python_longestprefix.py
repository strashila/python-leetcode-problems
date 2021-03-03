# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        
        if len(strs) <= 1:
            return ""
        elif len(strs) == 1:
            return strs[0]

        
        longest_prefix = ""

        first_word = strs[0]
        strs.remove(first_word)

        for i in range(0, len(first_word)+1):
            is_first_there = True
            for word in strs:
                if word[:i] != first_word[:i]:
                    is_first_there = False
            if is_first_there:
                longest_prefix = word[:i]
 
        return longest_prefix

s = Solution()

word_list =  ["flower","flower","flower","flower"]

print (s.longestCommonPrefix(word_list))