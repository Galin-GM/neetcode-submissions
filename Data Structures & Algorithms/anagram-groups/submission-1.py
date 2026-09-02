class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dt = {}

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            count = tuple(count)

            if count in dt:
                dt[count].append(word)    
            else:
                dt[count] = [word]

        return list(dt.values())