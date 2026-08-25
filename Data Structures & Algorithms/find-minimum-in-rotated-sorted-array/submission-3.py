class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[-1]

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] > minimum:
                l = mid + 1
            else:
                minimum = nums[mid]
                r = mid - 1
        return minimum           