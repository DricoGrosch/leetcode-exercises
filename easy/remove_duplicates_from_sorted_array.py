from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write_index = 1
        for i in range(1, len(nums)):
            current = nums[i]
            previous = nums[i - 1]
            if current != previous:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index
nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution().removeDuplicates(nums),nums)
