class Solution:
    def intToRoman(self, arabic_num: int) -> str:
        thousands = arabic_num // 1000
        hundrends = (arabic_num - thousands * 1000) // 100
        dozens = (arabic_num - (thousands * 1000) - (hundrends * 100)) // 10
        digits = arabic_num-(thousands * 1000) - (hundrends * 100) - (dozens * 10)

        digits_dict = {
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX"
        }

        dozens_dict = {
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC"
        }

        hundrends_dict = {
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM"
        }

        roman_num = ""
        for _ in range(thousands):
            roman_num += "M"

        if hundrends in hundrends_dict:
            roman_num += hundrends_dict[hundrends]

        if dozens in dozens_dict:
            roman_num += dozens_dict[dozens]

        if digits in digits_dict:
            roman_num += digits_dict[digits]

        return roman_num
        
s = Solution()

print (s.intToRoman(16))