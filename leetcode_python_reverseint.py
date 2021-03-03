# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:

        is_negative = False
        if x < 0:
            x = abs(x)
            is_negative = True

        modificator = 10
        reverse_num_list = []
        reversed_num = 0

        while modificator <= x:
            modificator *= 10
        
        while modificator > 1:
            digit = (x - ((x // modificator) * modificator)) // (modificator // 10)
            reverse_num_list.append(digit)
            modificator = modificator // 10

        i = 1
        for num in reverse_num_list:
            reversed_num = reversed_num + num*i
            i = i * 10     
        
        if is_negative:
            reversed_num = -reversed_num
        
        if abs(reversed_num) >= 2**31-1:
            return 0
        else:
            return reversed_num


s = Solution()
a = 1534236469
print (s.reverse(a))





