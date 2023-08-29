class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip() 
        if not s:
            return 0  
        
        sign = 1
        if s[0] in ['+', '-']:
            if s[0] == '-':
                sign = -1
            s = s[1:] 
        
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break 
        
        num = min(max(sign * num, -2**31), 2**31 - 1)
        
        return num
