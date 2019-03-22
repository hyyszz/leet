class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        ni = 0
        hi = 0
        rn = -1
        if needle == '':
            return 0
        
        while (hi < len(haystack)) & (ni < len(needle)):
                if haystack[hi] == needle[ni]:
                        hi += 1
                        ni += 1
                else:
                    hi = hi - ni + 1
                    ni = 0
                   
        if ni == len(needle):
            rn = hi - ni
        else :
            rn = -1
        
        return rn


s = Solution()
a = s.strStr(haystack='dabacddba', needle='dd')
print(a)

