from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for index,value in enumerate(nums2):
            nums1[m+index]=value
        nums1.sort()

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
Solution().merge(nums1,m,nums2,n)
print(nums1)