class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = r = 0
        substring = set()
        longest = 0

        while r < len(s):
            # invalid
            while s[r] in substring:
                substring.remove(s[l])
                l += 1

            # valid
            substring.add(s[r])
            longest = max(longest, len(substring))
            r += 1

        return longest
            