from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        valid_numbers = 1
        insert_index = 1
        for i in range(1, len(nums)):
            previous = nums[i-1]
            current = nums[i]
            if previous == current:
                counter+=1
            else:
                counter=1
            if counter <=2:
                nums[insert_index]=current
                insert_index+=1
                valid_numbers+=1
        return valid_numbers
        

        
nums=[1,1,1,2,2,3]
Solution().removeDuplicates(nums)
print(nums)


