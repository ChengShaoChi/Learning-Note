#set()：創一個無序且不重複的集合
class Solution:
    def findErrorNums(self, nums):
        n=len(nums)
        nset=set(nums)#去掉重複的數字
        dup=sum(nums)-sum(nset)
        missing=n*(n+1)//2-sum(nset)#//：取整數的除法
        return dup,missing
