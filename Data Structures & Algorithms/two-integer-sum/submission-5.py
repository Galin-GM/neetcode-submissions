class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dt = {}

        for idx, n in enumerate(nums):
            number_needed = target - n

            if number_needed in dt:
                i = dt.get(number_needed)
                return [i[0], idx]

            if n in dt:
                dt[n] = dt[n].append(idx)
            else:
                dt[n] = [idx]
