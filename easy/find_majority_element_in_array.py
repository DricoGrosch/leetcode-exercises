from collections import defaultdict
from typing import List
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         appearances={}
#         for value in nums:
#             if value not in appearances:
#                 appearances[value] =0
#             appearances[value] +=1
#         max_appearances = max(appearances.values())
#         index_of_max_appearances = list(appearances.values()).index(max_appearances)
#         return list(appearances.keys())[index_of_max_appearances]

# def get_value(key_par_array):
#     return key_par_array[1]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        
        appearances = defaultdict(int)
        for value in nums:
            appearances[value] += 1
            
        majority_element,majority_element_appearances = max(appearances.items(), key=lambda key_pair_array:key_pair_array[1])
        return majority_element

    
nums =[3,2,2]
response = Solution().majorityElement(nums)
print(response)
        