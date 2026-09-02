class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dt = defaultdict(list)
        
        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1

            dt[tuple(count)].append(word)

        return list(dt.values())