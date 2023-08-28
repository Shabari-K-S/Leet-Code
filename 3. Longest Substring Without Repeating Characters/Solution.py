class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        str_chk = ""

        for i in s:
            if i in str_chk:
                index = str_chk.index(i)
                str_chk = str_chk[index+1:]
            str_chk += i
            max_len = max(max_len, len(str_chk))

        return max_len
