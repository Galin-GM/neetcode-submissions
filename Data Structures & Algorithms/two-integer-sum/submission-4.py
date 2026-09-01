class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dt = {}

        for idx in range(len(nums)):
            number_needed = target - nums[idx]

            if number_needed in dt:
                i = dt.get(number_needed)
                j = dt.get(nums[idx])
                return [i[0], idx]

            if nums[idx] in dt:
                dt[nums[idx]] = (dt[nums[idx]]).append(idx)
            else:
                dt[nums[idx]] = [idx]
