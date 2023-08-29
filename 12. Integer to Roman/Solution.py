class Solution:
    def intToRoman(self, num: int) -> str:
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        
        roman_numeral = ""
        i = 0
        
        while num > 0:
            div = num // val[i]
            num %= val[i]
            
            while div > 0:
                roman_numeral += syms[i]
                div -= 1
            
            i += 1
        
        return roman_numeral