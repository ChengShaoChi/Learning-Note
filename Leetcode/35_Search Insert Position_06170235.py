class Solution:
    def searchInsert(self, nums: List[int], target: int):
        for i in range(len(nums)):
            cur = nums[i]
            if target <= cur:
                return i
                break
            else:
                i += 1
        return i
        
#如果都大於現在nums裡的數字，要記得return i，不然會變None。
