class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        # for sure equal length
        dt_s = {}
        dt_t = {}

        for i in range(len(s)):
            ch_s = s[i]
            ch_t = t[i]

            dt_s[ch_s] = 1 + dt_s.get(ch_s, 0)
            dt_t[ch_t] = 1 + dt_t.get(ch_t, 0)

        return dt_s == dt_t