

class Solution:
    next = []

    def calNext(self, needle:str):
        nlen = len(needle)
        j = 0
        k = -1
        self.next = [0] * nlen
        self.next[0] = -1
        while j < nlen - 1 :
            if (k == -1) | (needle[j] == needle[k]):
                j += 1
                self.next[j] = k + 1
                k = self.next[j]
            else:
                k = self.next[k]

    # kmp搜索算法
    def strStr(self, haystack: str, needle: str) -> int:
        self.calNext(needle)
        print(self.next)
        rn = 0
        hi = 0
        ni = 0
        while (hi < len(haystack)) & (ni < len(needle)):
            if (ni == -1) | (haystack[hi] == needle[ni]):
                hi += 1
                ni += 1
            else:
                ni = self.next[ni]
        if ni == len(needle):
            rn = hi - ni
        else:
            rn = -1
        return rn


s = Solution()
# s.calNext('abcdabde')
haystack = 'abacababc'
needle = 'abab'
r = s.strStr(haystack, needle)
print(r)
