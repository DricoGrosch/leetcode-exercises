from typing import List


class Solution:
    def jump(self,nums,current_index,max_index_reachable)->bool:
        available_jumps = nums[current_index]
        next_index = current_index + available_jumps  
        
        if next_index >= len(nums)-1:
            return True
        
        if next_index > max_index_reachable:
            max_index_reachable = next_index

        if current_index ==max_index_reachable and available_jumps == 0:
            return False
        
        return self.jump(nums,current_index+1,max_index_reachable)

    def canJump(self, nums: List[int]) -> bool:
        return self.jump(nums,0,nums[0])