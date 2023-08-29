class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}
        def method(i,j):
            if (i,j) not in mem:
                if j == len(p):
                    ans = i == len(s)
                else:
                    firstmatch = i < len(s) and p[j] in {s[i], "."}
                    if j+1 < len(p) and p[j+1] == "*":
                        ans = method(i,j+2) or firstmatch and method(i+1,j)
                    else:
                        ans = firstmatch and method(i+1,j+1)
                
                mem[i,j] = ans
            return mem[i,j]
        return method(0,0)
