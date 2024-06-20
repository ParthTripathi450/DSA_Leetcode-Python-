class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums)==1:
            return nums
        L=[]
        for i in range(len(nums)):
            L.append(nums[i])
        for i in range(len(nums)):
            pos=i
            new_pos=i+k
            if new_pos<len(nums):
                nums[new_pos]=L[i] 
            else:
                while new_pos>=len(nums):
                    new_pos=new_pos-len(nums)
                nums[new_pos]=L[i]
        """
        Do not return anything, modify nums in-place instead.
        """
        