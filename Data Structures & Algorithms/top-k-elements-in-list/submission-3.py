class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dt = {}

        for n in nums:
            dt[n] = dt.get(n, 0) + 1


        dt = sorted(dt.items(), key = lambda i: i[1], reverse=True)

        ans = []

        for pair in dt[:k]:
            ans.append(pair[0])

        return ans