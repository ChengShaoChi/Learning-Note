#錯的，無法滿足所有輸入
class Solution:
    def findErrorNums(self, nums):
        dup=0
        missing=0
        for i in range(len(nums)):
            if nums[i]==nums[i-1]:
                dup=nums[i]
                missing=nums[i-1]+1
        return dup,missing

#set()：創一個無序且不重複的集合
class Solution:
    def findErrorNums(self, nums):
        n=len(nums)
        nset=set(nums)#去掉重複的數字
        dup=sum(nums)-sum(nset)
        missing=n*(n+1)//2-sum(nset)#//：取整數的除法
        return dup,missing
