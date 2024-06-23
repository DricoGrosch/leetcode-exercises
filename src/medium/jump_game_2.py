from typing import List

class Solution:
    def get_next_index(self,nums,i,reachable_index)->int:
        max_reachable_index = 0
        response_index = i
        for j in range(i,reachable_index+1):
            temp_reachable_index = j + nums[j]
            if temp_reachable_index > len(nums)-1:
                return j
            if temp_reachable_index < reachable_index:
                continue
            if temp_reachable_index>max_reachable_index:
                max_reachable_index = temp_reachable_index
                response_index = j
        return response_index

    def jump(self, nums: List[int]) -> int:
        total_jumps = 0
        next_index_to_reach = 0
        for i in range(len(nums)-1):
            if i == len(nums)-1:
                break
            if i<next_index_to_reach:
                continue
            total_jumps+=1
            reachable_index_from_here = i+nums[i]
            if reachable_index_from_here >= len(nums)-1:
                break
            next_index_to_reach = self.get_next_index(nums,i,reachable_index_from_here)
        return total_jumps
    
solution = Solution()