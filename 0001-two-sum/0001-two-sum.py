class Solution(object):
    def twoSum(self, nums, target):
        k=len(nums)
        for i in range(k):
            for j in range(k):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        return [i,j]
       