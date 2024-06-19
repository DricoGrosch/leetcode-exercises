from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for index, value in enumerate(nums):
            counter = 1
            for _index,_value in enumerate(nums):
                if index==_index:
                    continue
                if value!=_value:
                    continue
                counter+=1
                if counter >2:
                    nums.remove(_value)
                
        return len(nums)
# nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
print(Solution().removeDuplicates(nums),nums)
