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

assert Solution().canJump([3,0,8,2,0,0,1]) == True
assert Solution().canJump([2,3,1,1,4]) == True
assert Solution().canJump([3,2,1,0,4]) == False
assert Solution().canJump([0]) == True
assert Solution().canJump([2,5,0,0]) == True