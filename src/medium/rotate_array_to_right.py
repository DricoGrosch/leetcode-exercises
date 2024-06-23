from typing import List
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         for _ in range(k):
#             aux = nums[0]
#             for i in range(1,len(nums)):
#                 current = nums[i]
#                 nums[i]=aux
#                 aux=current
#             nums[0]=aux

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         if k==0:
#             return
#         aux = nums[0]
#         for i in range(1,len(nums)):
#             current = nums[i]
#             nums[i]=aux
#             aux=current
#         nums[0]=aux
#         k-=1
#         self.rotate(nums,k)

    

# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         n = len(nums)
#         k = k % n  # In case k is greater than the length of nums
#         nums[:] = nums[-k:] + nums[:-k]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k==0:
            return
        current = nums.pop()
        nums.insert(0,current)
        k-=1
        self.rotate(nums,k)

nums = [1,2,3,4,5,6,7]
Solution().rotate(nums,3)
print(nums)