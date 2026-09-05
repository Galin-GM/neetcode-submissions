class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            
            mid = l + (r - l) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid

        #left is index of minimum
        left, right = 0, len(nums) - 1
        if nums[l] <= target and target <= nums[-1]:
            left = l 
        else:
            right = l-1          

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1